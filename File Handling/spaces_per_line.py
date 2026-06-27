file = open("sample.txt", "r")

for line in file:

    count = line.count(" ")

    print("Spaces:", count)

file.close()