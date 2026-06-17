file = open("sample.txt", "r")

content = file.read()

if len(content) == 0:
    print("File is Empty")
else:
    print("File is Not Empty")

file.close()