file = open("sample.txt", "r")

n = int(input("Enter number of characters: "))

content = file.read(n)

print("Content:")
print(content)

file.close()