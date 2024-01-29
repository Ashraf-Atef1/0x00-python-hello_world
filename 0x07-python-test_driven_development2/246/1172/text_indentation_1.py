#!/usr/bin/python3
""" Doc """

def text_indentation(text):
    """ Doc """
    text_update = str(text)
    after_new_line = False
    for c in text_update:
        if after_new_line:
            if c == " ":
                continue
            after_new_line = False
        if c == '.' or c == '?' or c == ':':
            print(c)
            print("")
            after_new_line = True
        else:
            print(c, end="")
