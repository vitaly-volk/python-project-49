from random import randint

START_RANDINT_FROM = 0
END_RANDINT_WITH = 100
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 0:
        return False
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def generate_question():
    random_input = randint(START_RANDINT_FROM, END_RANDINT_WITH)
    correct_answer = 'yes' if is_prime(random_input) else 'no'
    return (random_input, correct_answer)
