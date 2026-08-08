num = int(input("Enter a Number: "))

temp = num

while temp > 9:
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit
        temp = temp // 10

    temp = sum

if temp == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")