file = open("sample.txt", "r")

count = 0

for line in file:

    for ch in line:
        if ch.isdigit():
            count += 1
            break

print("Lines Containing Digits:", count)

file.close()