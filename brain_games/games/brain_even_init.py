from random import randint


START_RANDINT_FROM = 0
END_RANDINT_WITH = 100


def generate_question():
    random_input = randint(START_RANDINT_FROM, END_RANDINT_WITH)
    correct_answer = 'yes' if random_input % 2 == 0 else 'no'
    return (random_input, correct_answer)
