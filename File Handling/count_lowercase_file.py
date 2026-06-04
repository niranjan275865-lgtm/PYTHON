file = open("sample.txt", "r")

content = file.read()

count = 0

for ch in content:

    if ch.islower():
        count += 1

print("Number of Lowercase Letters:", count)

file.close()