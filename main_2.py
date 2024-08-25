import queue

def task(name, queue:queue.Queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield total
        print(f"Task {name} total: {total}")

def main():
    work_queue = queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [task("One", work_queue), task("Two", work_queue)]

    done = False
    while not done:
        for t in tasks:
            print(t)
            try:
                resp = next(t)
                # print(resp)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True
            print('mini end')
        
        print('end for')

if __name__ == "__main__":
    main()