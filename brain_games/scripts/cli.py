import prompt


def greeting():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name
