import sys
from ft_filter import ft_filter


def filterstring(words_list, size):
    '''return a new list removing words with a lenght under size'''
    return list(ft_filter(lambda word: len(word) > size, words_list))


def main(argv):
    '''Main de test et parsing'''
    try:
        if len(argv) != 3:
            raise AssertionError("AssertionError: \
Wrong number of arguments")
        if not all(x.isalnum() or x == ' ' for x in argv[1]):
            raise AssertionError(
                "AssertionError: First argument is not a valid string"
            )
        try:
            int(argv[2])
        except ValueError:
            raise AssertionError(
                "AssertionError: Second argument is not an integer"
            )
        print(filterstring(str(argv[1]).split(), int(argv[2])))
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main(sys.argv)
