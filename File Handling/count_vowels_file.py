file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content.lower():

    if ch in "aeiou":
        count += 1

print("Number of Vowels:", count)

file.close()