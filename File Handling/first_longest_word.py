file = open("sample.txt", "r")

content = file.read()

words = content.split()

longest = ""

for word in words:

    if len(word) > len(longest):
        longest = word

print("First Longest Word:", longest)

file.close()