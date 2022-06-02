#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

ops = ['+', '-', '*', '/']
argc = len(argv)
if __name__ == '__main__':
     if (argc - 1) < 3:
