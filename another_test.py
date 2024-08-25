import asyncio
import aiohttp
from codetiming import Timer

async def fetch_url(session, url):
    timer = Timer(text=f"Time elapsed for getting {url} : {{:.1f}}")
    print('Getting {url}'.format(url=url))
    timer.start()
    async with session.get(url) as response:
        response.raise_for_status()
        result = await response.json()
        timer.stop()
        return result

async def process_data(data, url):
    timer = Timer(text=f"Time elapsed for processing {url} : {{:.1f}}")
    print('processing data for {url}'.format(url=url))
    timer.start()
    data = {
        "id": data.get("id"),
        "title": data.get("title"),
        "userId": data.get("userId")
    }
    timer.stop()
    return data

async def fetch_and_process_url(session, url):
    data = await fetch_url(session, url)
    processed_data = await process_data(data, url)
    return processed_data

async def fetch_and_process_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_and_process_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    
    results = await fetch_and_process_all_urls(urls)
    for result in results:
        print(result)

# Run the main function
asyncio.run(main())
