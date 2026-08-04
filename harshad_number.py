num = int(input("Enter a Number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    temp = temp // 10

if num % sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")