file = open("sample.txt", "r")

for line in file:

    words = line.split()

    if words:
        longest = max(words, key=len)
        print("Longest Word:", longest)

file.close()