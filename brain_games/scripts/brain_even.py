#!/usr/bin/env python3


from brain_games import greetings
from brain_games import game_even


def main():
    name = greetings.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_even.game(name)


if __name__ == '__main__':
    main()
