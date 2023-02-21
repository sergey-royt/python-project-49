#!/usr/bin/env python3


from brain_games import greetings
from brain_games.games import game_calc


def main():
    name = greetings.welcome_user()
    print('What is the result of the expression?')
    game_calc.main(name)

if __name__ == '__main__':
    main()