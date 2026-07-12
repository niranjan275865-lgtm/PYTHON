file = open("sample.txt", "r")

count = 0

for line in file:

    text = line.strip()

    if text.isupper():
        count += 1

print("Uppercase Lines:", count)

file.close()