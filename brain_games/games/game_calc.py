import random


def rules():
    return 'What is the result of the expression?'


def main():
    operators = ['+', '-', '*']
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    op = operators[random.randint(0, 2)]
    question = f'{x} {op} {y}'
    result = str(eval(question))
    return (question, result)
