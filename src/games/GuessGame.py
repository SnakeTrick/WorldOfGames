# GuessGame.py
import random


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        """Generate a random number between 1 and difficulty"""
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        """Get the user's guess"""
        while True:
            try:
                guess = int(input(f"Guess the number (between 1 and {self.difficulty}): "))
                if 1 <= guess <= self.difficulty:
                    return guess
                print(f"Please enter a number between 1 and {self.difficulty}")
            except ValueError:
                print("Please enter a valid number")

    def compare_results(self, guess):
        """Compare user's guess with the secret number"""
        return guess == self.secret_number

    def play(self):
        """Play the game"""
        self.generate_number()
        guess = self.get_guess_from_user()
        return self.compare_results(guess)