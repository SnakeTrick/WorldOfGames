import random
import requests

def get_exchange_rate():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        rates = response.json()
        return rates["rates"]["ILS"]
    except Exception:
        print("Error fetching exchange rate. Using default rate of 3.5.")
        return 3.5

def get_money_interval(difficulty, amount, rate):
    total_value = amount * rate
    margin = 5 - difficulty
    return total_value - margin, total_value + margin

def get_guess_from_user(amount):
    while True:
        try:
            guess = float(input(f"Guess the value of {amount} USD in ILS: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def play(difficulty):
    rate = get_exchange_rate()
    amount = random.randint(1, 100)
    lower_bound, upper_bound = get_money_interval(difficulty, amount, rate)
    guess = get_guess_from_user(amount)
    if lower_bound <= guess <= upper_bound:
        print("You won!")
        return True
    else:
        print(f"You lost! The correct range was {lower_bound:.2f} - {upper_bound:.2f}.")
        return False
