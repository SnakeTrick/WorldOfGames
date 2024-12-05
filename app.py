from flask import Flask, render_template, request
from GuessGame import play as play_guess
from MemoryGame import play as play_memory
from CurrencyRouletteGame import play as play_currency_roulette

app = Flask(__name__)

@app.route('/')
def home():
    # Show the game selection page
    return render_template('play.html')

@app.route('/play', methods=['POST'])
def play():
    game_choice = request.form.get("game_choice")
    difficulty = request.form.get("difficulty")

    # Convert to integers and validate inputs
    try:
        game_choice = int(game_choice)
        difficulty = int(difficulty)
    except ValueError:
        return "Invalid input. Please enter numeric values.", 400

    if game_choice not in range(1, 4) or difficulty not in range(1, 6):
        return "Invalid input. Please select valid options.", 400

    # Game logic based on user's choice
    if game_choice == 1:
        # Start Memory Game (You would implement this logic in MemoryGame.py)
        return render_template('memory_game.html', difficulty=difficulty)
    elif game_choice == 2:
        # Start Guess Game
        result = play_guess(difficulty)  # Use the GuessGame play function
        if result:
            message = f"You won! The secret number was guessed correctly."
        else:
            message = f"You lost! The secret number was {random.randint(1, difficulty)}."
        return render_template('result.html', message=message)
    elif game_choice == 3:
        # Start Currency Roulette Game (You would implement this in CurrencyRouletteGame.py)
        return render_template('currency_roulette_game.html', difficulty=difficulty)

    return "Unknown game choice. Please try again.", 400

if __name__ == '__main__':
    app.run(debug=True)
