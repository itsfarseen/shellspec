#!/usr/bin/env python3
"""
A simple calculator script to demonstrate basic shellspec testing.
"""
import sys
import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero", file=sys.stderr)
        sys.exit(1)
    return a / b

def main():
    parser = argparse.ArgumentParser(description='Simple calculator')
    parser.add_argument('operation', choices=['add', 'sub', 'mul', 'div'])
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, help='Second number')
    
    args = parser.parse_args()
    
    operations = {
        'add': add,
        'sub': subtract,
        'mul': multiply,
        'div': divide
    }
    
    result = operations[args.operation](args.a, args.b)
    print(result)

if __name__ == '__main__':
    main()