file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:

    if ch == " ":
        count += 1

print("Number of Spaces:", count)

file.close()