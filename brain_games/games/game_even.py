from random import randint


GAME_NUMBER_RANGE_BOTTOM = 0
GAME_NUMBER_RANGE_TOP = 100


def get_rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number_to_check):
    return not number_to_check % 2

def get_result():
    number = randint(GAME_NUMBER_RANGE_BOTTOM, GAME_NUMBER_RANGE_TOP)

    if is_even(number):
        result = 'yes'
    else:
        result = 'no'
    return number, result
