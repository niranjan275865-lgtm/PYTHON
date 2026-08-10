num = int(input("Enter a Number: "))

square = num * num

digits = len(str(num))

right = square % (10 ** digits)
left = square // (10 ** digits)

if left + right == num:
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")