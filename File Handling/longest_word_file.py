file = open("sample.txt", "r")

content = file.read()

words = content.split()

longest = max(words, key=len)

print("Longest Word:", longest)

file.close()