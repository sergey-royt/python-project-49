import prompt


NUMBER_OF_ROUNDS = 3


def play_game(game):
    username = prompt.string('Welcome to the Brain Games! \
\nMay I have your name? ')
    print(f'Hello, {username}!')
    print(game.get_rules())

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_result()
        answer = prompt.string(f'Question: {question} \
\nYour answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"""'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.
Let's try again, {username}!""")
            return None
    print(f'Congratulations, {username}!')
