import threading
import time

def download(file):
    print(f"Downloading {file}...")
    time.sleep(2)
    print(f"{file} downloaded")

files = ["file1.txt", "file2.txt", "file3.txt"]

threads = []

for file in files:
    t = threading.Thread(target=download, args=(file,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
