file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:

    if not ch.isalnum() and not ch.isspace():
        count += 1

print("Number of Special Characters:", count)

file.close()