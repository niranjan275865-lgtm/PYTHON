file = open("sample.txt", "r")

lines = file.readlines()

for line in reversed(lines):
    print(line.strip())

file.close()