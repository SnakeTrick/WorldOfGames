# CurrencyRouletteGame.py
import random
import requests


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self, dollar_amount):
        """Calculate the valid interval for a guess"""
        try:
            # Using a free currency API
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            usd_to_ils = response.json()['rates']['ILS']

            total_value = dollar_amount * usd_to_ils
            interval = 5 - self.difficulty

            return (total_value - interval, total_value + interval)
        except:
            # Fallback to a fixed rate if API fails
            usd_to_ils = 3.5
            total_value = dollar_amount * usd_to_ils
            interval = 5 - self.difficulty
            return (total_value - interval, total_value + interval)

    def get_guess_from_user(self, dollar_amount):
        """Get user's guess for the conversion"""
        while True:
            try:
                guess = float(input(f"How many ILS is {dollar_amount}$? "))
                return guess
            except ValueError:
                print("Please enter a valid number")

    def play(self):
        """Play the currency roulette game"""
        dollar_amount = random.randint(1, 100)
        interval = self.get_money_interval(dollar_amount)
        guess = self.get_guess_from_user(dollar_amount)
        return interval[0] <= guess <= interval[1]