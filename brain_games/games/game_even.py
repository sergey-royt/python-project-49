from random import randint


def rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number_to_check):
    if not number_to_check % 2:
        return True
    return False


def game():
    GAME_NUMBER_RANGE_BOTTOM = 0
    GAME_NUMBER_RANGE_TOP = 100

    number = randint(GAME_NUMBER_RANGE_BOTTOM, GAME_NUMBER_RANGE_TOP)

    if is_even(number):
        result = 'yes'
    else:
        result = 'no'
    return (number, result)
