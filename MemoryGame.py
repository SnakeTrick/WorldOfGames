import random


def play(difficulty):
    # Generate the sequence of random numbers
    sequence = [random.randint(1, 101) for _ in range(difficulty)]

    # Return the sequence to be displayed by the frontend
    return sequence