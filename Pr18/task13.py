with open("input.txt", "r", encoding="utf-8") as source, open("numbered.txt", "w", encoding="utf-8") as target:
    for index, line in enumerate(source, start=1):
        target.write(f"{index}. {line}")
