file = open("sample.txt", "r")

for line in file:
    print("Characters:", len(line.strip()))

file.close()