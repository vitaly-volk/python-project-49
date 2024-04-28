#!/usr/bin/env python3


from brain_games.engine import run_game
from brain_games.games.brain_gcd import generate_question


QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(QUESTION, generate_question)


if __name__ == '__main__':
    main()
