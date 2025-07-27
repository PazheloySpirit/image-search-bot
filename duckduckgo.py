import aiohttp
from bs4 import BeautifulSoup

async def search_images_duckduckgo(query, max_results=3):
    search_url = f"https://duckduckgo.com/?q={query}&iax=images&ia=images"
    headers = {"User-Agent": "Mozilla/5.0"}

    async with aiohttp.ClientSession() as session:
        async with session.get(search_url, headers=headers) as resp:
            html = await resp.text()

    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all("script")
    image_urls = []

    for script in scripts:
        if 'var o' in script.text:
            parts = script.text.split('"image":"')
            for part in parts[1:max_results+1]:
                url = part.split('"')[0].replace("\\", "")
                if url.startswith("http"):
                    image_urls.append(url)
            break

    return image_urls