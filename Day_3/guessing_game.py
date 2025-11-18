import random 

print("Welcome to the Number Guessing Game!")

# Random number between 1 and 50
number_to_guess = random.randint(1, 50)

guess = None
attempts = 0

while guess != number_to_guess:
    guess = int(input("Enter your guess (1-50): "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

