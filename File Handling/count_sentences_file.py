file = open("sample.txt", "r")

content = file.read()

sentences = content.split(".")

count = len(sentences) - 1

print("Number of Sentences:", count)

file.close()