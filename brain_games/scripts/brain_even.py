#!/usr/bin/env python3


from brain_games.engine import run_game
from ..import_ import generate_question_even


ATTEMPTS_NUMBER = 3
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(ATTEMPTS_NUMBER, QUESTION, generate_question_even)


if __name__ == '__main__':
    main()
