file = open("sample.txt", "r")

content = file.read()

words = content.split()

unique_words = set(words)

print("Number of Unique Words:", len(unique_words))

file.close()