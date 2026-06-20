file = open("sample.txt", "rb")

content = file.read()

print("Number of Bytes:", len(content))

file.close()