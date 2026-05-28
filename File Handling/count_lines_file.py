file = open("sample.txt", "r")

lines = file.readlines()

count = len(lines)

print("Number of lines:", count)

file.close()