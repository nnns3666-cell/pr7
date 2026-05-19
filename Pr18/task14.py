with open("input.txt", "r", encoding="utf-8") as source, open("clean.txt", "w", encoding="utf-8") as target:
    for line in source:
        if line.strip():
            target.write(line)
