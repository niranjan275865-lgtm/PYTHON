file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:

    if ch != " " and ch != "\n":
        count += 1

print("Characters (Without Spaces):", count)

file.close()