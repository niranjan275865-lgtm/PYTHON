numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = max(numbers)
smallest = min(numbers)

difference = largest - smallest

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Difference:", difference)