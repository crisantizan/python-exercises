def is_palindrome(phrase):
    invert = phrase[::-1]

    return invert == phrase


def main():
    phrase = input("Insert a word/phrase: ").replace(' ', '').lower()

    if is_palindrome(phrase):
        print('\u001b[32mIs palindrome')
    else:
        print('\u001b[31mNon-palindrome')
    pass


if __name__ == '__main__':
    main()
