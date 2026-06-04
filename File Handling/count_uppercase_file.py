file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:

    if ch.isupper():
        count += 1

print("Number of Uppercase Letters:", count)

file.close()