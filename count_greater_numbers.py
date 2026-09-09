numbers = list(map(int, input("Enter numbers separated by space: ").split()))
limit = int(input("Enter the limit: "))

count = 0

for num in numbers:
    if num > limit:
        count += 1

print("Numbers greater than limit:", count)