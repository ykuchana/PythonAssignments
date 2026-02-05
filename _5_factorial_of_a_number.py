"""
Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
"""

# 1. Using while loop

# def factorial(num):
#     result = 1
#     while num > 1:
#         result *= num
#         num -= 1
#     return result

# 2. using recursive function

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         pass
#         result = num * factorial(num - 1)
#         return result

# 3. by importing math module

def factorial(num):
    import math
    return math.factorial(num)

if __name__ == "__main__":
    while True:
        number = input("Enter a number: ")
        if number.isnumeric():
            print(f"Factorial of {number} is: {factorial(int(number))}.")
            break
        else:
            print("Only  non-negative integer values are allowed to calculated the factorial.")
            print()