#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        if argc == 1:
            print(f"{argc} argument:")
        else:
            print(f"{argc} arguments:")
        for arg_num, arg_name in enumerate(argv[1:], 1):
            print("{:d}: {:s}".format(arg_num, arg_name))
