num = int(input("Enter a decimal number: "))

if num >= 0:
    binary = bin(num)[2:]
    print("Binary number:", binary)
else:
    print("Please enter a non-negative number")