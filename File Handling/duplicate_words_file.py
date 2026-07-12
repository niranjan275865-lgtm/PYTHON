file = open("sample.txt", "r")

content = file.read()

words = content.split()

printed = []

print("Duplicate Words:")

for word in words:

    if words.count(word) > 1 and word not in printed:
        print(word)
        printed.append(word)

file.close()