import prompt
from brain_games import greetings


def main(game):
    player_name = greetings.welcome_user()
    print(game.rules())

    try_number = 1

    while try_number <= 3:
        result = game.main()
        answer = prompt.string(f'Question: {result[0]}\nYour answer: ')
        if answer == result[1]:
            print('Correct!')
            try_number += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. \
Correct answer was '{result[1]}'.
Let's try again, {player_name}!""")
            return None
    print(f'Congratulations, {player_name}!')
