secret = 22
guess=0

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("Bravo")
    else:
        print("Sorry " + str(guess) + " is not the secret number.")

