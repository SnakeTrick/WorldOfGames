import random


# This function generates a secret number based on the difficulty.
def generate_number(difficulty):
    return random.randint(1, difficulty)


# This function compares the user's guess to the secret number.
def compare_results(user_guess, secret_number):
    return user_guess == secret_number


# Main game function.
def play(difficulty):
    # Generate a secret number
    secret_number = generate_number(difficulty)

    # Prompt the user for their guess (in this case, assume you get it from Flask)
    user_guess = int(input(f"Guess a number between 1 and {difficulty}: "))

    # Compare the guess and check if the user won
    if compare_results(user_guess, secret_number):
        return True  # User won
    else:
        return False  # User lost
