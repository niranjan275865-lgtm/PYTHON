file = open("sample.txt", "r")

content = file.read()

unique_chars = set(content)

print("Number of Unique Characters:", len(unique_chars))

file.close()