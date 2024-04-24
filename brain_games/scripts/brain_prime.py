#!/usr/bin/env python3


from brain_games.scripts.brain_interface import run_the_game
from ..import_ import generate_question_prime


ATTEMPTS_NUMBER = 3
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question_prime)


if __name__ == '__main__':
    main()
