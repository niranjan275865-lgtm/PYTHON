num = int(input("Enter a Number: "))

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


reverse = int(str(num)[::-1])

if is_prime(num) and is_prime(reverse):
    print("Emirp Number")
else:
    print("Not an Emirp Number")