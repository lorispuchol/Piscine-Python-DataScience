import sys


def main(argv):

    '''
displays the sums of upper-case characters, lower-case characters, \
punctuation characters, digits and spaces in a string
    '''
    try:
        if len(argv) > 2:
            raise AssertionError("AssertionError: more than \
                                 one argument is provided")
        if len(argv) <= 1:
            txt = input("What is the text to count?\n")
        else:
            txt = argv[1]
        marks = "\'!\"#$%&()*+,-./:;<=>?@[]^_`{|}~"
        sum_uppers = sum(1 for c in txt if c.isupper())
        sum_lowers = sum(1 for c in txt if c.islower())
        sum_marks = sum(1 for c in txt if c in marks) # OU import string and check in string.punctuation 
        sum_spaces = sum(1 for c in txt if c == ' ')
        sum_digits = sum(1 for c in txt if c.isdigit())
        total = len(txt)

        print("The text contains", total, "characters:")
        print(sum_uppers, "upper letters")
        print(sum_lowers, "lower letters")
        print(sum_marks, "punctuation marks")
        print(sum_spaces, "spaces")
        print(sum_digits, "digits")

    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main(sys.argv)
