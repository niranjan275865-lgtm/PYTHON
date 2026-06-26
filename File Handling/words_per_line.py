file = open("sample.txt", "r")

for line in file:
    words = line.split()
    print("Words in line:", len(words))

file.close()