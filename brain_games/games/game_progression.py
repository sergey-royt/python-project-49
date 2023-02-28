from random import randint


def rules():
    return 'What number is missing in the progression?'


def main():
    progression = [randint(0, 10)]
    hidden_index = randint(0, 10)
    progression_step = randint(2, 10)

    for element in range(10):
        progression.append(progression[element] + progression_step)

    hidden_number = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(str(item) for item in progression)
    return (question, hidden_number)
