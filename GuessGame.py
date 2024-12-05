import random

def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print(f"Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def compare_results(secret_number, user_guess):
    return secret_number == user_guess

def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if compare_results(secret_number, user_guess):
        print("You won!")
        return True
    else:
        print(f"You lost! The correct number was {secret_number}.")
        return False
