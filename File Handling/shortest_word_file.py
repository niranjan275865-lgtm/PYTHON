file = open("sample.txt", "r")

content = file.read()

words = content.split()

shortest = min(words, key=len)

print("Shortest Word:", shortest)

file.close()