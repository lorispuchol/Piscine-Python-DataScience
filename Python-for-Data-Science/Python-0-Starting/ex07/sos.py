import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def decrypt(str):
    '''return a morse string converted from an alplanumeric string'''
    newStr = ""

    for x in str:
        newStr += NESTED_MORSE[x.upper()]
    return newStr


def main(argv):
    '''Parsing and test'''
    try:
        if len(argv) != 2:
            raise AssertionError("AssertionError: \
Wrong number of arguments")
        if not all(str(x).isalnum() or x == ' ' for x in argv[1]):
            raise AssertionError(
                "AssertionError: First argument is not a valid string"
            )
        print(decrypt(str(argv[1])))
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main(sys.argv)
