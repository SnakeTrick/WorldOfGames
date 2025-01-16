# Score.py
from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    """Add score for winning a game"""
    points_of_winning = (difficulty * 3) + 5

    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            current_score = int(f.read() or 0)
    except:
        current_score = 0

    new_score = current_score + points_of_winning

    with open(SCORES_FILE_NAME, 'w') as f:
        f.write(str(new_score))