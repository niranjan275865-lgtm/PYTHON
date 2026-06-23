file = open("sample.txt", "r")

content = file.read()

words = content.split()

max_count = 0
most_frequent = ""

for word in words:

    count = words.count(word)

    if count > max_count:
        max_count = count
        most_frequent = word

print("Most Frequent Word:", most_frequent)

file.close()