import sys
from ft_filter import ft_filter


def main():
    """Check arguments and use filter to keep words greater than length"""

    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")

        sentence = sys.argv[1]
        length = int(sys.argv[2])
        words = sentence.split(" ")

        # list expression to keep words without special characters
        clean_words = [word for word in words if word.isalpha()]

        # lambda to create short function in argument
        greater_words = ft_filter(lambda word: len(word) > length, clean_words)

        print(list(greater_words))

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
