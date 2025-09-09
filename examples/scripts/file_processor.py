#!/usr/bin/env python3
"""
File processing utility to demonstrate file I/O testing with shellspec.
"""
import sys
import os
import argparse

def count_lines(filename):
    try:
        with open(filename, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'", file=sys.stderr)
        sys.exit(1)

def count_words(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return len(content.split())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'", file=sys.stderr)
        sys.exit(1)

def create_backup(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        sys.exit(1)
    
    backup_name = filename + '.bak'
    try:
        with open(filename, 'r') as src, open(backup_name, 'w') as dst:
            dst.write(src.read())
        print(f"Backup created: {backup_name}")
    except Exception as e:
        print(f"Error creating backup: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='File processing utility')
    parser.add_argument('command', choices=['lines', 'words', 'backup'])
    parser.add_argument('filename', help='File to process')
    
    args = parser.parse_args()
    
    if args.command == 'lines':
        print(count_lines(args.filename))
    elif args.command == 'words':
        print(count_words(args.filename))
    elif args.command == 'backup':
        create_backup(args.filename)

if __name__ == '__main__':
    main()