with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()
    print("Количество слов:", len(words))
