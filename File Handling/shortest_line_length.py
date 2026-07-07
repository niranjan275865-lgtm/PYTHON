file = open("sample.txt", "r")

lines = file.readlines()

min_length = len(lines[0].strip())

for line in lines:

    length = len(line.strip())

    if length < min_length:
        min_length = length

print("Shortest Line Length:", min_length)

file.close()