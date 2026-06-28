file = open("sample.txt", "r")

count = 0

for line in file:

    line = line.strip()

    if line and line[0].lower() in "aeiou":
        count += 1

print("Lines Starting with Vowel:", count)

file.close()