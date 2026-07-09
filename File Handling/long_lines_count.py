file = open("sample.txt", "r")

count = 0

for line in file:

    if len(line.strip()) > 10:
        count += 1

print("Lines Longer Than 10 Characters:", count)

file.close()