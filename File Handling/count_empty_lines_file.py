file = open("sample.txt", "r")

lines = file.readlines()

count = 0

for line in lines:
    if line.strip() == "":
        count += 1

print("Number of Empty Lines:", count)

file.close()