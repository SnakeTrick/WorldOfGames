from Live import load_game, welcome
from GuessGame import play as play_guess
from MemoryGame import play as play_memory
from CurrencyRouletteGame import play as play_currency_roulette

print(welcome("Guy"))

game_choice, difficulty = load_game()

if game_choice == 1:
    play_memory(difficulty)
elif game_choice == 2:
    play_guess(difficulty)
elif game_choice == 3:
    play_currency_roulette(difficulty)
