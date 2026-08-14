numbers = [10, 15, 20, 25, 30, 35]

sum = 0

for num in numbers:
    if num % 2 != 0:
        sum += num

print("Sum of Odd Numbers:", sum)