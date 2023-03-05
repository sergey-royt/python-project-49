import prompt


def engine(game):
    username = prompt.string('Welcome to the Brain Games! \
\nMay I have your name? ')
    print(f'Hello, {username}!')
    print(game.rules())

    QUESTION_POSITION = 0
    ANSWER_POSITION = 1
    NUMBER_OF_ROUNDS = 3

    for _ in range(NUMBER_OF_ROUNDS):
        result = game.game()
        answer = prompt.string(f'Question: {result[QUESTION_POSITION]} \
\nYour answer: ')
        if answer == result[ANSWER_POSITION]:
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(. \
Correct answer was '{result[ANSWER_POSITION]}'.
Let's try again, {username}!""")
            return None
    print(f'Congratulations, {username}!')
