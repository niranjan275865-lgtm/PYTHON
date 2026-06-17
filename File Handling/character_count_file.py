file = open("sample.txt", "r")

content = file.read()

ch = input("Enter character to count: ")

count = content.count(ch)

print("Frequency of", ch, ":", count)

file.close()