#!/usr/bin/python3.4
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    lenght = len(sys.argv)
    if lenght != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    x = int(sys.argv[1])
    y = int(sys.argv[3])
    sign = sys.argv[2]

    operator = {'+': add, '-': sub,
                '*': mul, '/': div}
    for i in operator:
        if sign == i:
            res = operator[i](x, y)
            print('{:d} {} {:d} = {:d}'.format(x, sign, y, res))
            exit(0)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
