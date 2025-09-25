import sys


NESTED_MORSE = {" ": "/ ",
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "0": "-----"}


def main():
    """Check the arguments and change the sentence to Morse code"""

    try:
        if len(sys.argv) != 2:
            raise AssertionError("Assertion Error: the arguments are bad")

        sentence = sys.argv[1]
        sentence_upper = sentence.upper()

        for char in sentence_upper:
            if not char.isalnum() and char != " ":
                raise AssertionError("Assertion Error: the arguments are bad")

        i = 0
        morse_code = ""
        for char in sentence_upper:
            if char in NESTED_MORSE:
                if i > 0:
                    morse_code += " "
                morse_code += NESTED_MORSE[char]
                i += 1

        print(morse_code)

    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
