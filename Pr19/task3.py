import threading

def worker():
    for _ in range(5):
        print(threading.current_thread().name)

threads = []

for i in range(3):
    t = threading.Thread(target=worker, name=f"Thread-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()
