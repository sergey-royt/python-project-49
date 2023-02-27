import prompt


def main(result, question, player_name):
    answer = prompt.string(f'Question: {question}\nYour answer: ')
    if result == answer:
        print('Correct!')
        return True
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was '{result}'.
Let's try again, {player_name}!""")
        return False
