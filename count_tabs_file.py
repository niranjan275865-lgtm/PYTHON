file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:
    if ch == "\t":
        count += 1

print("Number of Tabs:", count)

file.close()