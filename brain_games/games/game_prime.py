from random import randint
from brain_games import games_logic


def is_prime(number):
    if number == 1:
        return 'yes'
    else:
        for i in range(2, number):
            if number % i == 0:
                return 'no'
        return 'yes'


def main(player_name):
    try_number = 1

    while try_number <= 3:
        number = randint(1, 100)
        answer = is_prime(number)
        if games_logic.main(answer, number, player_name):
            try_number += 1
        else:
            return None
    print(f'Congratulations, {player_name}!')
