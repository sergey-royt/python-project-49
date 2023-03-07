#!/usr/bin/env python3


from brain_games import games_logic
from brain_games.games import game_calc


def main():
    games_logic.play_game(game_calc)


if __name__ == '__main__':
    main()
