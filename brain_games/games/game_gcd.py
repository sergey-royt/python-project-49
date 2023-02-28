import random
import math


def rules():
    return 'Find the greatest common divisor of given numbers.'


def main():
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    result = str(math.gcd(x, y))
    question = f'{x} {y}'
    return (question, result)
