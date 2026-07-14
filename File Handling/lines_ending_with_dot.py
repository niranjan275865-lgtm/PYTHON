file = open("sample.txt", "r")

count = 0

for line in file:
    line = line.strip()

    if line.endswith("."):
        count += 1

print("Lines Ending with '.' :", count)

file.close()