file = open("sample.txt", "r")

content = file.read()

words = content.split()

count = len(words)

print("Number of words:", count)

file.close()