file = open("sample.txt", "r")

count = 0

for line in file:

    for ch in line.lower():

        if ch in "aeiou":
            count += 1
            break

print("Lines Containing Vowels:", count)

file.close()