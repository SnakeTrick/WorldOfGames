import random
import time

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    print(f"Enter {difficulty} numbers separated by space:")
    while True:
        try:
            user_input = list(map(int, input().split()))
            if len(user_input) == difficulty:
                return user_input
            else:
                print(f"Please enter exactly {difficulty} numbers.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def is_list_equal(sequence, user_list):
    return sequence == user_list

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Memorize this sequence:")
    print(sequence)
    time.sleep(0.7)
    print("\n" * 100)
    user_list = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_list):
        print("You won!")
        return True
    else:
        print(f"You lost! The correct sequence was {sequence}.")
        return False
