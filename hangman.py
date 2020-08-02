from random import randint
from os import name, system
from time import sleep

CLIPS = [
    '''
            +---+
            |   |
                |
                |
                |
                |
                |
                ==========
    ''',
    '''
            +---+
            |   |
            0   |
                |
                |
                |
                |
                ==========
    ''',
    '''
            +---+
            |   |
            0   |
           /    |
                |
                |
                |
                ==========
    ''',
    '''
            +---+
            |   |
            0   |
           /|   |
                |
                |
                |
                ==========
    ''',
    '''
            +---+
            |   |
            0   |
           /|\\  |
                |
                |
                |
                ==========
    ''',
    '''
            +---+
            |   |
            0   |
           /|\\  |
            |   |
                |
                |
                ==========
    ''',
    '''
            +---+
            |   |
            0   |
           /|\\  |
            |   |
           /    |
                |
                ==========
    ''',
    '''
            +---+
            |   |
            0   |
           /|\\  |
            |   |
           / \\  |
                |
                ==========
    ''',
]

WORDS = ['house', 'computer', 'mouse', 'tree', 'country',
         'microsoft', 'freezer', 'colombia', 'constitution', ]


def random_word():
    index = randint(0, len(WORDS)-1)
    return WORDS[index]


def clear():
    # for Windows
    if name == 'nt':
        _ = system('cls')
    # Linux, Mac
    else:
        _ = system('clear')


def main():
    print('***** Welcome to Hangman Game *****')
    print('Are you ready?')
    sleep(2)
    word = random_word()
    counter = 0
    chars = ['-'] * len(word)

    while True:
        clear()
        print(CLIPS[counter])
        print(chars)

        input_text = input('Enter one letter: ')
        input_letter = input_text[0].lower()

        found = False
        for index, letter in enumerate(word):
            if input_letter == letter:
                chars[index] = letter
                found = True

        if not found:
            counter += 1

        if counter < 7:
            try:
                # non-winner
                chars.index('-')
                continue
            except:
                # winner
                print(chars)
                print("\u001b[32mYou're winner!")
                break
        else:
            clear()
            print(CLIPS[counter])
            print(
                '\n\u001b[31mYou lose! the correct word was: "{}"'.format(word))
            break


if __name__ == '__main__':
    main()
