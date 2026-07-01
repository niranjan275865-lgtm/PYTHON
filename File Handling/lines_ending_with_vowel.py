file = open("sample.txt", "r")

count = 0

for line in file:

    line = line.strip()

    if line and line[-1].lower() in "aeiou":
        count += 1

print("Lines Ending with Vowel:", count)

file.close()