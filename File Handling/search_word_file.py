file = open("sample.txt", "r")

content = file.read()

word = input("Enter word to search: ")

if word in content:
    print("Word Found")
else:
    print("Word Not Found")

file.close()