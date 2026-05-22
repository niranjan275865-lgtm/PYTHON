def leap(year):

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True

    return False


year = int(input("Enter a year: "))

if leap(year):
    print("Leap Year")

else:
    print("Not a Leap Year")