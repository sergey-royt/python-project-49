import random


GAME_NUMBER_RANGE_BOTTOM = 0
GAME_NUMBER_RANGE_TOP = 100


def get_rules():
    return 'What is the result of the expression?'


def get_result():
    operators = ['+', '-', '*']
    x = random.randint(GAME_NUMBER_RANGE_BOTTOM, GAME_NUMBER_RANGE_TOP)
    y = random.randint(GAME_NUMBER_RANGE_BOTTOM, GAME_NUMBER_RANGE_TOP)
    op = random.choice(operators)
    question = f'{x} {op} {y}'
    result = str(eval(question))
    return question, result
