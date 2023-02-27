import random
import math
from brain_games import games_logic


def main(player_name):
    try_number = 1
    while try_number <= 3:
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        answer = str(math.gcd(x, y))
        question = f'{x} {y}'
        if games_logic.main(answer, question, player_name):
            try_number += 1
        else:
            return None
    print(f'Congratulations, {player_name}!')
