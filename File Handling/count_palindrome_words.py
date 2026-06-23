file = open("sample.txt", "r")

content = file.read()

words = content.split()

count = 0

for word in words:

    if word == word[::-1]:
        count += 1

print("Number of Palindrome Words:", count)

file.close()