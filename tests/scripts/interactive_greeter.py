#!/usr/bin/env python3
import sys
name = input("What is your name? ")
print(f"Hello, {name}!")
age = input("What is your age? ")
print(f"You are {age} years old.")
fail = input("Should I fail? (y/n) ")
if fail == "y":
    print("Failing as requested.", file=sys.stderr)
    sys.exit(1)
print("Exiting normally.")
sys.exit(0)
