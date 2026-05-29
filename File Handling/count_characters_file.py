file = open("sample.txt", "r")

content = file.read()

count = len(content)

print("Number of Characters:", count)

file.close()