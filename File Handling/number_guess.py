secret = 7

guess = int(input("Guess the Number (1-10): "))

if guess == secret:
    print("Correct! You Won.")
else:
    print("Wrong! The Correct Number is", secret)