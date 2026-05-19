with open("input.txt", "r", encoding="utf-8") as source, open("upper.txt", "w", encoding="utf-8") as target:
    target.write(source.read().upper())
