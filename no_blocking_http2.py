"""Context switch with no-blocking call with python asyncio
Execution time is equal to the longest task"""

import asyncio
import aiohttp
from codetiming import Timer

urls = [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://apple.com",
        "http://microsoft.com",
        "http://facebook.com",
        "http://twitter.com",
]

async def task(name, url):
    timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')
    async with aiohttp.ClientSession() as session:
        print('Getting {url}'.format(url=url))
        timer.start()
        async with session.get(url) as response:
            await response.text()        
        timer.stop()


async def main():
    tasks = []
    for index, url in enumerate(urls):
        tasks.append(task(f"task-{index}-{url}", url))
    
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())