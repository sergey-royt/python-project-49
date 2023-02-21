import random
from brain_games import games_logic


def is_even(number_to_check):
    if number_to_check % 2 == 0:
        return 'yes'
    return 'no'


def game(user_name):
    try_number = 1
    while try_number <= 3:
        number = random.randint(0, 100)
        if games_logic.main(is_even(number), number, user_name):
            try_number += 1
        else:
            return None
    print(f'Congratulations, {user_name}!')
