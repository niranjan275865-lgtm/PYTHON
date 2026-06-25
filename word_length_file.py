file = open("sample.txt", "r")

content = file.read()

words = content.split()

for word in words:
    print(word, ":", len(word))

file.close()