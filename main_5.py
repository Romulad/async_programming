"""2 - Context switch with no-blocking call with python asyncio
Execution time is equal to the longest task"""

import asyncio
from codetiming import Timer


async def task(name, delay):
    timer = Timer(text=f'Task {name} elapsed time: {{:.1f}}')
    timer.start()
    await asyncio.sleep(delay)
    timer.stop()

async def main():
    tasks = []
    for index, delay in enumerate([15, 10, 5, 2]):
        tasks.append(task(f"task-{index}-{delay}", delay))
    
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())