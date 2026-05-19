with open("input.txt", "r", encoding="utf-8") as file1, open("copy.txt", "w", encoding="utf-8") as file2:
    file2.write(file1.read())
