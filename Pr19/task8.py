import threading
import queue
import time

q = queue.Queue()

def worker():
    while not q.empty():
        task = q.get()
        print(f"{threading.current_thread().name} processing {task}")
        time.sleep(1)
        q.task_done()

for i in range(5):
    q.put(f"Task-{i+1}")

threads = []

for i in range(3):
    t = threading.Thread(target=worker, name=f"Worker-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()
