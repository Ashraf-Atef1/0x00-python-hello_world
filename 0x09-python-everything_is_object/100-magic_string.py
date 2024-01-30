#!/usr/bin/python3
def magic_string(s="BestSchool"):
    return "\n".join([((f"{s}, " * i or "") + s) for i in range(10)])
