"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""
# 1. using either os.path module or pathlib.Path module
"""
from pathlib import Path

file_name = Path("sample.txt")

if not file_name.exists():
    print(f"Error: The file '{file_name}' was not found.")
    # raise Exception(f"Error: The file '{file_name}' was not found.")
else:
    print("Reading file content.")
    with open("sample.txt", 'rt') as fh:
        lines = fh.readlines()
        for i in range(0,len(lines)):
            print(f"Line {i+1}: {lines[i].rstrip("\n")}")
"""

# using try-except
file_name = "sample.txt"
# file_name = input("Enter your file name without extension: ") + ".txt"
# print(file_name)

try:
    with open(file_name, 'rt') as fh:
        data = fh.readlines()
        if len(data) > 0:
            print("Reading file content.")
            for i in range(0, len(data)):
                print(f"Line {i + 1}: {data[i].rstrip("\n")}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")