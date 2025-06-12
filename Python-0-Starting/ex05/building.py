import sys

def count_str_and_print(string: str):
    """Count the sum of upper-case character, lower-case character, punctuation character, digits, space and displays its"""
    size = len(string)
    upper_case = lower_case = punctuation = digits = space = 0

    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        elif char.isdigit():
            digits += 1
        elif char == ' ' or char == '\n':
            space += 1
        else:
            punctuation += 1

    print("The text contains", size, "characters:")
    print(upper_case, "upper letters")
    print(lower_case, "lower letters")
    print(punctuation, "punctuations marks")
    print(digits, "digits")
    print(space, "spaces")

def main():
    try:
        if len(sys.argv) == 1:
            raise ValueError("please, can you provide a string in one argument?")
        if len(sys.argv) > 2:
            raise ValueError("AssertionError: more than one argument is provided")
        count_str_and_print(sys.argv[1])
    except ValueError as e:
        print(e)
        return

if __name__ == "__main__":
    main()
