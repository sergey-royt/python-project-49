import random
import math


def rules():
    return 'Find the greatest common divisor of given numbers.'


def game():
    GAME_NUMBER_RANGE_BOTTOM = 0
    GAME_NUMBER_RANGE_TOP = 100

    x = random.randint(GAME_NUMBER_RANGE_BOTTOM, GAME_NUMBER_RANGE_TOP)
    y = random.randint(GAME_NUMBER_RANGE_BOTTOM, GAME_NUMBER_RANGE_TOP)
    result = str(math.gcd(x, y))
    question = f'{x} {y}'
    return (question, result)
