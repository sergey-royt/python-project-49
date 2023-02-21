import random
import prompt


def is_even(number_to_check):
    if number_to_check % 2 == 0:
        return 'yes'
    return 'no'


def game(user_name):
    try_number = 1
    while try_number <= 3:
        number = random.randint(0, 100)
        user_answer = prompt.string(f'Question: {number}\nYour answer: ')
        if user_answer == is_even(number):
            print('Correct!')
            try_number += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{is_even(number)}'.\nLet's try again, {user_name}!")
            return None
    print(f'Congratulations, {user_name}!')
           