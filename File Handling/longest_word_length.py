file = open("sample.txt", "r")

content = file.read()

words = content.split()

longest = 0

for word in words:

    if len(word) > longest:
        longest = len(word)

print("Longest Word Length:", longest)

file.close()