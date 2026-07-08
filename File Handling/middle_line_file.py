file = open("sample.txt", "r")

lines = file.readlines()

middle = len(lines) // 2

print("Middle Line:")
print(lines[middle].strip())

file.close()