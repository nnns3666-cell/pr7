import threading
import time

def background():
    while True:
        print("Daemon thread working...")
        time.sleep(1)

daemon = threading.Thread(target=background, daemon=True)
daemon.start()

time.sleep(3)
print("Main program finished")
