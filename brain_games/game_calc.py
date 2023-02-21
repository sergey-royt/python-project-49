import random
from brain_games import games_logic


def addition(a, b):
    result = a + b
    return result


def subtraction(a, b):
    result = a - b
    return result


def multiplication(a, b):
    result = a * b
    return result


def main(player_name):
    operators = ['+', '-', '*']
    try_number = 1
    while try_number <= 3:
        x = random.randint(0,100)
        y = random.randint(0, 100)
        op = operators[random.randint(0, 2)]
        question = f'{x} {op} {y}'
        if op == '+':
            if games_logic.main(str(addition(x, y)), question, player_name):
                try_number += 1
            else:
                return None
        elif op == '-':
            if games_logic.main(str(subtraction(x, y)), question, player_name):
                try_number += 1
            else:
                return None
        elif op == '*':
            if games_logic.main(str(multiplication(x, y)), question, player_name):
                try_number += 1
            else:
                return None
    print(f'Congratulations, {player_name}!')
       