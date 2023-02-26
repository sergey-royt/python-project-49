from random import randint
from brain_games import games_logic


def main(player_name):
    try_number = 1
    
    while try_number <= 3:
        progression = [randint(0, 10)]
        hidden_index = randint(0, 10)
        progression_step = randint(2, 10)
    
        for element in range(10):
            progression.append(progression[element] + progression_step)
    
        hidden_number = str(progression[hidden_index])
        progression[hidden_index] = '..'
        question = ' '.join(str(item) for item in progression)
        if games_logic.main(hidden_number, question, player_name):
            try_number += 1
        else:
            return None    
    print(f'Congratulations, {player_name}!')
