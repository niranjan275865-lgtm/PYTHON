file = open("sample.txt", "r")

content = file.read()

word = input("Enter word to count: ")

count = content.split().count(word)

print("Frequency:", count)

file.close()