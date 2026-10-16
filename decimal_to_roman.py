num = int(input("Enter a number (1-3999): "))

if 1 <= num <= 3999:
    values = [
        1000, 900, 500, 400, 100, 90,
        50, 40, 10, 9, 5, 4, 1
    ]

    symbols = [
        "M", "CM", "D", "CD", "C", "XC",
        "L", "XL", "X", "IX", "V", "IV", "I"
    ]

    roman = ""

    for i in range(len(values)):
        while num >= values[i]:
            roman += symbols[i]
            num -= values[i]

    print("Roman numeral:", roman)
else:
    print("Please enter a number from 1 to 3999")