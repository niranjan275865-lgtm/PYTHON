file = open("sample.txt", "r")

lines = file.readlines()

longest = max(lines, key=len)

print("Longest Line:")
print(longest.strip())

file.close()