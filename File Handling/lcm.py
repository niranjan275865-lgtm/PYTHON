num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

greater = max(num1, num2)

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        print("LCM =", greater)
        break
    greater += 1