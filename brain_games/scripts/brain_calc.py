"""BrainCalc"""
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')

    count = 0
    while count < 3:
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
        actions = ['+', '-', '*']
        action = actions[randint(0, len(actions) - 1)]
        answer = 0
        if action == '+':
            answer = number_1 + number_2
        elif action == '-':
            answer = number_1 - number_2
        elif action == '*':
            answer = number_1 * number_2

        user_answer = int(prompt.string(f'Question: {number_1} {action} {number_2} '))
        print(f'Your answer: {user_answer}')

        if answer != user_answer:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{answer}".')
            print(f'Let\'s try again, {name}')
            return
        count += 1
        print('Correct!')
    print(f'Congratulations, {name}')

if __name__ == '__main__':
    main()