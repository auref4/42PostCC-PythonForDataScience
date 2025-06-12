import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 2:
    try:
        nb = int(sys.argv[1])
        if nb % 2 == 0:
            print("I'm Odd")
        else:
            print("I'm Even")
    except ValueError:
        print("AssertionError: argument is not integer")
