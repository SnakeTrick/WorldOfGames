from flask import Flask, render_template, request, redirect, url_for
from Live import welcome, load_game
from GuessGame import play as play_guess
from MemoryGame import play as play_memory
from CurrencyRouletteGame import play as play_currency_roulette

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", message="Welcome to World of Games!")

@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        game_choice = int(request.form["game_choice"])
        difficulty = int(request.form["difficulty"])
        if game_choice == 1:
            result = play_memory(difficulty)
        elif game_choice == 2:
            result = play_guess(difficulty)
        elif game_choice == 3:
            result = play_currency_roulette(difficulty)
        else:
            result = False
        return render_template("result.html", success=result)
    return render_template("play.html")

if __name__ == "__main__":
    app.run(debug=True)
