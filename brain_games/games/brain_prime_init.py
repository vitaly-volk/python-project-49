from random import randint


def isPrime(number):
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
    random_input = randint(0, 100)
    correct_answer = 'yes' if isPrime(random_input) else 'no'
    return (random_input, correct_answer)
