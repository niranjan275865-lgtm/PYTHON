file = open("sample.txt", "r")

words = file.read().split()

count = 0

for word in words:
    if word == word[::-1]:
        count += 1

print("Palindrome Words:", count)

file.close()