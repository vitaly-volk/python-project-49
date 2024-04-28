#!/usr/bin/env python3


from brain_games.engine import run_game
from ..import_ import generate_question_calc


ATTEMPTS_NUMBER = 3
QUESTION = 'What is the result of the expression?'


def main():
    run_game(ATTEMPTS_NUMBER, QUESTION, generate_question_calc)


if __name__ == '__main__':
    main()
