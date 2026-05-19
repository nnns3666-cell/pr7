class SafeFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, "r", encoding="utf-8")
            return self.file
        except FileNotFoundError:
            print("Ошибка: файл не найден")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("File closed")

with SafeFile("input.txt") as file:
    if file:
        print(file.read())
