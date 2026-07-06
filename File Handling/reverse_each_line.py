file = open("sample.txt", "r")

for line in file:
    print(line.strip()[::-1])

file.close()