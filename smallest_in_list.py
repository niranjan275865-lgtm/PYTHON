numbers = [25, 10, 45, 18, 60, 32]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest Element =", smallest)