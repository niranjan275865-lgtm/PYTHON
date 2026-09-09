num = int(input("Enter a number: "))

num = abs(num)

while num >= 10:
    num = num // 10

print("First digit:", num)