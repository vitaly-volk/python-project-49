def main():
    from random import randint
    name = input("May I have your name? ")
    print(f"hello, {name}")
    attempts = 0
    result = True
    while result != False and attempts<3:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        number = randint(0,1000)
        print(f"Question: {number}")
        answer = input("Your answer: ")
        if number % 2 != 0:
            correct_answer = "no"
        else:
            correct_answer = "yes"
        if (answer == "yes" or answer == "Yes") and correct_answer == "no":
            result = False
        if (answer == "no" or answer == "No") and correct_answer == "yes":
            result = False
        if answer not in ["yes", "Yes", "no", "No"]:
            result = False
        if result == False:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
        else:
            print("Correct!")
            attempts+=1
        if attempts == 3:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()

