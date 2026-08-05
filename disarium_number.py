num = int(input("Enter a Number: "))

digits = str(num)

sum = 0

for i in range(len(digits)):
    sum += int(digits[i]) ** (i + 1)

if sum == num:
    print("Disarium Number")
else:
    print("Not a Disarium Number")