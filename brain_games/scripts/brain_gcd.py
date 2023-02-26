#!/usr/bin/env python3


from brain_games import greetings
from brain_games.games import game_gcd


def main():
    name = greetings.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_gcd.main(name)


if __name__ == '__main__':
    main()
