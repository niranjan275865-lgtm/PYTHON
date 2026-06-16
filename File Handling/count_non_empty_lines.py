file = open("sample.txt", "r")

count = 0

for line in file:
    if line.strip() != "":
        count += 1

print("Number of Non-Empty Lines:", count)

file.close()