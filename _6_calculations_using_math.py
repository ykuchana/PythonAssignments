"""
Task 2: Using the Math Module for Calculations

Problem Statement: Write a Python program that:
-----------------------------------------------
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
	-   Square root of the number
	-   Natural logarithm (log base e) of the number
	-   Sine of the number (in radians)
3.   Displays the calculated results.
"""

# simple approach with with print()
import math
number = int(input("Enter a number: "))

print(f"Square root: {math.sqrt(number)}")
print(f"Logarithm: {math.log(number)}")
print(f"Sine: {math.sin(number)}")

# using functions
# Square root of the number
# def sqareRoot(num):
#     return math.sqrt(number)
#
# # Natural logarithm (log base e) of the number
# def logBase10(num):
#     return math.log10(number)
#
# # Sine of the number (in radians)
# def sineInRadians(num):
#     return math.sin(number)
#
# # importing math module
# import math

# Performing the calculations
# if __name__ == "__main__":
#     while True:
#         number = input("Enter a number: ")
#
#         if number.isnumeric():
#             number = int(number)
#             print(f"Square root: {sqareRoot(number)}")
#             print(f"Logarithm: {logBase10(number)}")
#             print(f"Sine: {sineInRadians(number)}")
#             break
#         else:
#             print("Invalid number. Please try again!")
#             print()


