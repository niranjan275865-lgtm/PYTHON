file = open("sample.txt", "r")

count = 0

for line in file:

    line = line.strip()

    if line and line[-1].isdigit():
        count += 1

print("Lines Ending with Digit:", count)

file.close()