file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:
    if ch.isalpha():
        count += 1

print("Number of Alphabets:", count)

file.close()