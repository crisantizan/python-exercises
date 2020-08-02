def exists(char, chars):
    return char in chars


def char_counter(chars):
    found = None
    for index, char in enumerate(chars):
        if exists(char, chars[index + 1:]):
            found = char
            break

    return found


def main():
    chars = input('Enter characters: ')
    result = char_counter(chars)

    if result is None:
        print('None of the characters is repeated')
    else:
        print('The first repeated character is: {}'.format(result.upper()))


if __name__ == '__main__':
    main()
