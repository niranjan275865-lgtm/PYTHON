file = open("sample.txt", "r")

word = input("Enter the word to search: ")

count = 0

for line in file:

    if word in line:
        count += 1

print("Lines containing the word:", count)

file.close()