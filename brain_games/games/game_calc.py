import random
from brain_games import games_logic


def main(player_name):
    operators = ['+', '-', '*']
    try_number = 1
    while try_number <= 3:
        x = random.randint(0,100)
        y = random.randint(0, 100)
        op = operators[random.randint(0, 2)]
        question = f'{x} {op} {y}'
        if games_logic.main(str(eval(question)), question, player_name):
            try_number += 1
        else:
            return None    
    print(f'Congratulations, {player_name}!')
       