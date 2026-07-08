file = open("sample.txt", "r")

count = 0

for line in file:

    text = line.strip()

    if text.isdigit():
        count += 1

print("Numeric Lines:", count)

file.close()