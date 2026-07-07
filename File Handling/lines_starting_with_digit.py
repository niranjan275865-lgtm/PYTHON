file = open("sample.txt", "r")

count = 0

for line in file:

    line = line.strip()

    if line and line[0].isdigit():
        count += 1

print("Lines Starting with Digit:", count)

file.close()