#!/usr/bin/env python3


from brain_games import greetings
from brain_games.games import game_prime


def main():
    name = greetings.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    game_prime.main(name)


if __name__ == '__main__':
    main()
