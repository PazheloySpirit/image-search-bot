import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import InputMediaPhoto
from duckduckgo import search_images_duckduckgo

BOT_TOKEN = "7217913314:AAH0jdX0YH3dpaL30nDHwxNcN-pHAsLk4fI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    query = message.text.strip()
    await message.reply("🔍 Іду шукати картинки...")
    images = await search_images_duckduckgo(query)

    if not images:
        await message.reply("Нічого не знайшов.")
        return

    media = [InputMediaPhoto(url) for url in images]
    await bot.send_media_group(chat_id=message.chat.id, media=media)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())