import threading
import multiprocessing
import time

def task():
    sum(range(1, 1000000))

# Потоки
start = time.time()

threads = [threading.Thread(target=task) for _ in range(2)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Threading:", time.time() - start)

# Процессы
start = time.time()

processes = [multiprocessing.Process(target=task) for _ in range(2)]

for p in processes:
    p.start()

for p in processes:
    p.join()

print("Multiprocessing:", time.time() - start)
