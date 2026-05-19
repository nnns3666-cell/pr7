from datetime import datetime

with open("log.txt", "a", encoding="utf-8") as file:
    file.write(f"{datetime.now()} - Program started\n")
