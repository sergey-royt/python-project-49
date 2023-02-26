#!/usr/bin/env python3


from brain_games import greetings
from brain_games.games import game_progression


def main():
    name = greetings.welcome_user()
    print('What number is missing in the progression?')
    game_progression.main(name)
    

if __name__ == '__main__':
    main()
