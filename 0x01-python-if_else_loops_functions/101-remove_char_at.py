#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str):
        new_str = list(str)
        del new_str[n]
        str = "".join(new_str)
    return str