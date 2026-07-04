file = open("sample.txt", "r")

for line in file:
    print(line.strip(), ":", len(line.strip()))

file.close()