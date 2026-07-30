numbers = [25, 10, 45, 18, 60, 32]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest Element =", largest)