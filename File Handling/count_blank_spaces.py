file = open("sample.txt", "r")

content = file.read()

count = content.count(" ")

print("Number of Blank Spaces:", count)

file.close()