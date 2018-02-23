#!/usr/bin/env python3

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            if token == '+':
                 arg1 = stack.pop()
                 arg2 = stack.pop()
                 return(arg1 + arg2)
            elif token == '-':
                 arg2 = stack.pop()
                 arg1 = stack.pop()
                 return(arg1 - arg2)

def main():
    while True:
       print(calculate(input("rmp calc> ")))

if __name__ == '__main__':
    main()
