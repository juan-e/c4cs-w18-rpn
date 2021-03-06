#!/usr/bin/env python3
import operator
import readline

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
}

# This is a great calculator, honestly the best
def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
    if len(stack) != 1:
        raise TypeError

    return stack.pop()
def main():
    while True:
       try:
           print(calculate(input("rmp calc> ")))
       except KeyError:
           # print('\033[31m' + 'Error:')
           print('Please only enter numbers and operators:')
           for op in operators:
               print(op)
           # print(Style.RESET_ALL)

if __name__ == '__main__':
    main()
