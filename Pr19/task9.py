from multiprocessing import Process

def calculate():
    total = sum(range(1, 100001))
    print("Sum:", total)

p1 = Process(target=calculate)
p2 = Process(target=calculate)

p1.start()
p2.start()

p1.join()
p2.join()
