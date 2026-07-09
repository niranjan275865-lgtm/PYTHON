file = open("sample.txt", "r")

lines = file.readlines()

for i in range(0, len(lines), 2):
    print(lines[i].strip())

file.close()