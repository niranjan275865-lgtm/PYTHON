file = open("sample.txt", "r")

lines = file.readlines()

total_words = 0

for line in lines:
    total_words += len(line.split())

average = total_words / len(lines)

print("Average Words Per Line:", average)

file.close()