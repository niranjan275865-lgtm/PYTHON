file = open("sample.txt", "r")

lines = file.readlines()

max_words = 0
result = ""

for line in lines:

    words = len(line.split())

    if words > max_words:
        max_words = words
        result = line

print("Line with Maximum Words:")
print(result.strip())

file.close()