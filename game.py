import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        # Prompt the user to input their guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Compare the guess to the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            # User has guessed the number correctly
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
            print(f"It took you {attempts} attempts to guess the number.")
            break

# Run the game
if __name__ == "__main__":
    guess_the_number()
