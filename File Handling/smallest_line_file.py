file = open("sample.txt", "r")

lines = file.readlines()

smallest = min(lines, key=len)

print("Smallest Line:")
print(smallest.strip())

file.close()