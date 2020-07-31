from random import randint

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


def main():
    print('***** Welcome to Hangman Game *****')
    print(random_word())


if __name__ == '__main__':
    main()
