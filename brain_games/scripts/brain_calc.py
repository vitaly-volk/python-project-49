#!/usr/bin/env python3


from random import randint, choice
from brain_games.scripts.brain_interface import run_the_game
from ..import_ import generate_question_calc


ATTEMPTS_NUMBER = 3
QUESTION = 'What is the result of the expression?'

def main():
    run_the_game(ATTEMPTS_NUMBER, QUESTION, generate_question_calc)


if __name__ == '__main__':
    main()
