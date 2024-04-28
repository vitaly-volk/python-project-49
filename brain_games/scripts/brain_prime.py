#!/usr/bin/env python3


from brain_games.engine import run_game
from brain_games.games.brain_prime import generate_question


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(QUESTION, generate_question)


if __name__ == '__main__':
    main()
