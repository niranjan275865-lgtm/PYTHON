file = open("sample.txt", "r")

lines = file.readlines()

max_length = 0

for line in lines:
    length = len(line.strip())

    if length > max_length:
        max_length = length

print("Length of Longest Line:", max_length)

file.close()