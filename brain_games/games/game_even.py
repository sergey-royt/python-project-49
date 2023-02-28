from random import randint


def rules():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number_to_check):
    if not number_to_check % 2:
        return 'yes'
    return 'no'


def main():
    number = randint(0, 100)
    result = is_even(number)
    return (number, result)
