#!/usr/bin/env python3


from brain_games.engine import run_game
from ..import_ import generate_question_prog


QUESTION = 'What number is missing in the progression?'


def main():
    run_game(QUESTION, generate_question_prog)


if __name__ == '__main__':
    main()
