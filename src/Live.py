# Live.py

def welcome(name):
    """Welcome the player to World of Games"""
    return f"""Hello {name} and welcome to the World of Games (WoG).
Here you can find many cool games to play."""


def load_game():
    """Load and start the chosen game with specified difficulty"""
    while True:
        print("""Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")

        try:
            game_choice = int(input())
            if game_choice not in [1, 2, 3]:
                print("Please choose a valid game number between 1-3")
                continue

            print("Please choose game difficulty from 1 to 5:")
            difficulty = int(input())
            if difficulty not in range(1, 6):
                print("Please choose a valid difficulty between 1-5")
                continue

            # Import games only when needed
            if game_choice == 1:
                from MemoryGame import MemoryGame
                game = MemoryGame(difficulty)
            elif game_choice == 2:
                from GuessGame import GuessGame
                game = GuessGame(difficulty)
            else:
                from CurrencyRouletteGame import CurrencyRouletteGame
                game = CurrencyRouletteGame(difficulty)

            # Play the game and handle scoring
            won = game.play()
            if won:
                from Score import add_score
                add_score(difficulty)
            return

        except ValueError:
            print("Please enter valid numbers")