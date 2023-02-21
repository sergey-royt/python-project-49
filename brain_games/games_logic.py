import prompt


def games_routine(answer, question, player_name):
    user_answer = prompt.string(f'Question: {question}\nYour answer: ')
    if user_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {player_name}!")
        return False
