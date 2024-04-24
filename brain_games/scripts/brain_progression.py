#!/usr/bin/env python3


from brain_games.scripts.brain_interface import run_the_game
from ..import_ import generate_question_prog


ATTEMPTS_NUMBER = 3
QUESTION = 'What number is missing in the progression?'


def main():
    run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question_prog)


if __name__ == '__main__':
    main()
