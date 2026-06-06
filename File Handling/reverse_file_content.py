file = open("sample.txt", "r")

content = file.read()

print("Reversed Content:")
print(content[::-1])

file.close()