start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

total = 0

for i in range(start, end + 1):
    total += i

print("Sum =", total)