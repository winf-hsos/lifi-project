import random

# TODO: Generate a random whole number
number = random.randint(0, 100)

guess = input("Please guess: ")
guess = int(guess)

count = 1

# TODO: Start looping and ask for guesses until the guess is correct
while guess != number:

    # TODO: Check if the guess is high or low
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    
    # TODO: Ask the user for a guess
    guess = input("Please guess again: ")
    guess = int(guess)

    count = count + 1

# TODO: Print number guesses
print(f"Congratulations! Your guess is correct! It took you { count } attempts")


