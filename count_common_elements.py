list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

count = 0

for item in list1:
    if item in list2:
        count += 1

print("Number of Common Elements:", count)