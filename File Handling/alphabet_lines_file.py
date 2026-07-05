file = open("sample.txt", "r")

count = 0

for line in file:

    text = line.strip().replace(" ", "")

    if text.isalpha():
        count += 1

print("Alphabet Only Lines:", count)

file.close()