file = open("sample.txt", "r")

content = file.read()

print("Uppercase:")
print(content.upper())

print("\nLowercase:")
print(content.lower())

file.close()