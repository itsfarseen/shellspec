#!/usr/bin/env python3
"""
Interactive calculator script to demonstrate pexpect testing with shellspec.
"""
import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero!")
        return None
    return a / b

def show_menu():
    print("\n=== Interactive Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Show history")
    print("6. Clear history")
    print("q. Quit")
    print("==============================")

def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    history = []
    print("Welcome to Interactive Calculator!")
    
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'q' or choice == 'quit':
            print("Thank you for using Interactive Calculator!")
            break
        elif choice == '1':
            a, b = get_numbers()
            if a is not None and b is not None:
                result = add(a, b)
                print(f"Result: {a} + {b} = {result}")
                history.append(f"{a} + {b} = {result}")
        elif choice == '2':
            a, b = get_numbers()
            if a is not None and b is not None:
                result = subtract(a, b)
                print(f"Result: {a} - {b} = {result}")
                history.append(f"{a} - {b} = {result}")
        elif choice == '3':
            a, b = get_numbers()
            if a is not None and b is not None:
                result = multiply(a, b)
                print(f"Result: {a} * {b} = {result}")
                history.append(f"{a} * {b} = {result}")
        elif choice == '4':
            a, b = get_numbers()
            if a is not None and b is not None:
                result = divide(a, b)
                if result is not None:
                    print(f"Result: {a} / {b} = {result}")
                    history.append(f"{a} / {b} = {result}")
        elif choice == '5':
            if history:
                print("\n--- Calculation History ---")
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")
                print("---------------------------")
            else:
                print("No calculations in history.")
        elif choice == '6':
            history.clear()
            print("History cleared!")
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()