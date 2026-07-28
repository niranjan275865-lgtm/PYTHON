numbers = [10, 20, 10, 30, 20, 10]

checked = []

for num in numbers:
    if num not in checked:
        print(num, "appears", numbers.count(num), "times")
        checked.append(num)