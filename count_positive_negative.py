numbers = list(map(int, input("Enter numbers separated by space: ").split()))

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)