file = open("sample.txt", "r")

for line in file:

    words = line.split()

    if len(words) > 0:
        print(words[0])

file.close()