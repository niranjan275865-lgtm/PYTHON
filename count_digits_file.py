file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:

    if ch.isdigit():
        count += 1

print("Number of Digits:", count)

file.close()