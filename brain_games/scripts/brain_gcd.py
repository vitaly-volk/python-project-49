#!/usr/bin/env python3


from brain_games.engine import run_game
from ..import_ import generate_question_gcd


ATTEMPTS_NUMBER = 3
QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(ATTEMPTS_NUMBER, QUESTION, generate_question_gcd)


if __name__ == '__main__':
    main()
