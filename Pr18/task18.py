count = 0

with open("log.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "ERROR" in line:
            count += 1

print("Количество ошибок:", count)
