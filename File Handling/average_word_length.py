file = open("sample.txt", "r")

content = file.read()

words = content.split()

total = 0

for word in words:
    total += len(word)

average = total / len(words)

print("Average Word Length:", average)

file.close()