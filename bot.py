import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from duckduckgo_search import ddg_images

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "7217913314:AAH0jdX0YH3dpaL30nDHwxNcN-pHAsLk4fI"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привіт! Надішли мені будь-який запит, я знайду картинки.")

def image_search(update: Update, context: CallbackContext):
    query = update.message.text
    if not query:
        update.message.reply_text("Введи текст для пошуку картинок.")
        return
    results = ddg_images(query, max_results=3)
    if not results:
        update.message.reply_text("Нічого не знайшов.")
        return
    for img in results:
        update.message.bot.send_photo(chat_id=update.message.chat_id, photo=img['image'])

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("search", image_search))
    dp.add_handler(CommandHandler("img", image_search))
    dp.add_handler(CommandHandler("find", image_search))
    dp.add_handler(CommandHandler("pic", image_search))
    # Для звичайного тексту як пошуку
    dp.add_handler(MessageHandler(None, image_search))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
