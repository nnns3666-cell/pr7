import threading
import queue

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)
        print("Produced:", i)

def consumer():
    while not q.empty():
        item = q.get()
        print("Consumed:", item)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t1.join()

t2.start()
t2.join()
