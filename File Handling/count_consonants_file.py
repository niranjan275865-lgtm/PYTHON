file = open("sample.txt", "r")

content = file.read().lower()

count = 0

for ch in content:

    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Number of Consonants:", count)

file.close()