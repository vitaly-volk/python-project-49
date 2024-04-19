#!/usr/bin/env python3


from random import randint
from ..brain_interface import run_the_game


ATTEMPTS_NUMBER = 3
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    random_input = randint(0, 1000)
    correct_answer = "yes" if random_input % 2 == 0 else "no"
    return (random_input, correct_answer)


def main():
    run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question)


if __name__ == '__main__':
    main()
