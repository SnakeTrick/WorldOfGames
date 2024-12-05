import random
import requests

def get_currency_rate():
    # You can use any free API to get the exchange rate, for example:
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return data['rates']['ILS']

def play(difficulty):
    currency_rate = get_currency_rate()
    generated_amount = random.randint(1, 100)
    interval = (currency_rate * generated_amount) * (1 - (5 - difficulty)/100), (currency_rate * generated_amount) * (1 + (5 - difficulty)/100)
    return generated_amount, interval