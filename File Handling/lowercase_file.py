file = open("sample.txt", "r")

content = file.read()

print(content.lower())

file.close()