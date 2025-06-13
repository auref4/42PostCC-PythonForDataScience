import sys


def count_str_and_print(string: str):
    """Count and display upper-case, lower-case, punctuation, digits, space"""
    size = len(string)
    upper_case = lower_case = punctuation = digits = space = 0

    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        elif char == ' ' or char == '\n':
            space += 1
        elif char.isdigit():
            digits += 1
        else:
            punctuation += 1

    print("The text contains", size, "characters:")
    print(upper_case, "upper letters")
    print(lower_case, "lower letters")
    print(punctuation, "punctuation marks")
    print(space, "spaces")
    print(digits, "digits")


def main():
    """Main, handle errors and call necessary functions """
    try:
        if len(sys.argv) == 1:
            print("What is the text to count ?")
            text = sys.stdin.readline()
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise ValueError("AssertionError: more than 1 argument provided")
        count_str_and_print(text)
    except ValueError as e:
        print(e)
        return


if __name__ == "__main__":
    main()
