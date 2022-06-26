#!/usr/bin/env python
from brain_games.scripts import cli


def main():
    print('Welcome to the Brain Games!')
    user_name = cli.greeting()


if __name__ == '__main__':
    main()
