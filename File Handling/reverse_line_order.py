file = open("sample.txt", "r")

lines = file.readlines()

for line in lines[::-1]:
    print(line.strip())

file.close()