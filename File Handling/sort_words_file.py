file = open("sample.txt", "r")

content = file.read()

words = content.split()

words.sort()

print("Words in Alphabetical Order:")

for word in words:
    print(word)

file.close()