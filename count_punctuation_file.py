import string

file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:
    if ch in string.punctuation:
        count += 1

print("Number of Punctuation Marks:", count)

file.close()