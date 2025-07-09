import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 3

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("You have 3 tries to guess it correctly.")

while attempts > 0:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong guess. Try again! Attempts left: {attempts}")
        else:
            print(f"Game Over! The correct number was {secret_number}.")