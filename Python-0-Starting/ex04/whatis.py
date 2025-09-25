import sys


try:
    len = len(sys.argv)
    if len > 2:
        raise AssertionError("AssertionError: more than one argument is provided")
    if len == 2:
        if not sys.argv[1].isdigit():
            raise AssertionError("AssertionError: argument is not an integer")
        nb = int(sys.argv[1])
        if nb % 2 == 0:
            print("I'm Odd")
        else:
            print("I'm Even")

except Exception as e:
    print(e)
