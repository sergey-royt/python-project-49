from random import randint


def rules():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return 'yes'
    else:
        for i in range(2, number):
            if number % i == 0:
                return 'no'
        return 'yes'


def main():
    number = randint(1, 100)
    result = is_prime(number)
    return (number, result)
