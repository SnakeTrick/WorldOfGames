# MemoryGame.py
import random
import time
import os
from Utils import screen_cleaner


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        """Generate a random sequence of numbers"""
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):
        """Get sequence guess from user"""
        numbers = []
        for i in range(self.difficulty):
            while True:
                try:
                    num = int(input(f"Enter number {i + 1}: "))
                    numbers.append(num)
                    break
                except ValueError:
                    print("Please enter a valid number")
        return numbers

    def is_list_equal(self, list1, list2):
        """Compare two lists"""
        return list1 == list2

    def play(self):
        """Play the memory game"""
        sequence = self.generate_sequence()
        print("Remember this sequence:")
        print(sequence)
        time.sleep(0.7)
        screen_cleaner()

        user_sequence = self.get_list_from_user()
        return self.is_list_equal(sequence, user_sequence)
