#!/usr/bin/env python3


from brain_games.scripts.brain_interface import run_the_game
from ..import_ import generate_question_gcd


ATTEMPTS_NUMBER = 3
QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question_gcd)


if __name__ == '__main__':
    main()
