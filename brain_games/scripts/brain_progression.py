#!/usr/bin/env python3


from brain_games.engine import run_game
from brain_games.games.brain_prog import generate_question


QUESTION = 'What number is missing in the progression?'


def main():
    run_game(QUESTION, generate_question)


if __name__ == '__main__':
    main()
