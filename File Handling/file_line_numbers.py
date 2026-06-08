file = open("sample.txt", "r")

line_no = 1

for line in file:
    print(line_no, ":", line.strip())
    line_no += 1

file.close()