from random import randint



GAME_NUMBER_RANGE_BOTTOM = 1
GAME_NUMBER_RANGE_TOP = 100


def get_rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True


def get_result():
    number = randint(GAME_NUMBER_RANGE_BOTTOM, GAME_NUMBER_RANGE_TOP)

    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'
    return number, result
