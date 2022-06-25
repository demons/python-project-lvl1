"""Docs"""
import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name

def show_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')

def start_game(name, steps = 3):
    current_step = 0
    while current_step < steps:
        some_number = randint(1, 20)
        answer = 'yes' if some_number % 2 == 0 else 'no'
        print(f'Question: {some_number}')
        users_answer = prompt.string('Your answer: ')

        if answer != users_answer.lower():
            print(f'"{users_answer}" is wrong ;(. Correnct answer was "{answer}".\nLet\'s try again, {name}!')
            return
        print('Correct!')
        current_step += 1
    print(f'Congratulations, {name}')

def main():
    name = welcome_user()
    show_rules()
    start_game(name)


if __name__ == '__main__':
    main()