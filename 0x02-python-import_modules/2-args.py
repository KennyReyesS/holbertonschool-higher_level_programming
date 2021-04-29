#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n_arg = len(sys.argv) - 1
    if n_arg == 1:
        print("{} Argument.".format(n_arg))
    elif n_arg < 1:
        print("{} Arguments.".format(n_arg))
    else:
        print("{} Arguments.".format(n_arg))
    for i in range(1, len(sys.argv)):
        if i > 0:
            print("{}: {}".format(i, sys.argv[i]))
        else:
            print(end="")
