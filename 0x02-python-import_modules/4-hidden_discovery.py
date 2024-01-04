#!/usr/bin/python3
import dis
import codeop
import sys

def print_names(filename):
    with open(filename, 'rb') as file:
        code = compile(file.read(), filename, 'exec')

    names = set()
    
    def gather_names(oparg):
        nonlocal names
        if isinstance(oparg, str) and not oparg.startswith('__'):
            names.add(oparg)
            
    dis.disassemble(code, None, gather_names=gather_names)
    
    return names

if __name__ == "__main__":
    filename = "hidden_4.pyc"
    names = sorted(print_names(filename))
    
    for name in names:
        print(name)
