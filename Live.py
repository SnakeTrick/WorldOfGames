def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    while True:
        try:
            game_choice = int(input("Enter your choice (1-3): "))
            if 1 <= game_choice <= 3:
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Invalid difficulty. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return game_choice, difficulty
