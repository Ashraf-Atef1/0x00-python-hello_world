#!/usr/bin/python3
def multiple_returns(sentence = ""):
    str_length = len(sentence)
    if str_length:
        return str_length, sentence[0]
    else:
        return str_length, "None"
