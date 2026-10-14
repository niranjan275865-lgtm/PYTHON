num = int(input("Enter a decimal number: "))

if num >= 0:
    octal = oct(num)[2:]
    print("Octal number:", octal)
else:
    print("Please enter a non-negative number")