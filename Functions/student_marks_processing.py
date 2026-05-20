from functools import reduce

marks = [85, 42, 76, 90, 35, 67, 95, 48]

# Find toppers (marks >= 90)
toppers = list(filter(lambda x: x >= 90, marks))

# Find failed students (marks < 40)
failed = list(filter(lambda x: x < 40, marks))

# Calculate average
total = reduce(lambda x, y: x + y, marks)

average = total / len(marks)

print("Student Marks:", marks)
print("Toppers:", toppers)
print("Failed Students:", failed)
print("Class Average:", average)