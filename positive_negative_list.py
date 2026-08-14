numbers = [10, -5, 20, -8, 15, -2]

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive Numbers:", positive)
print("Negative Numbers:", negative)