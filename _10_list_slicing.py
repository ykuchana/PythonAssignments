"""
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""

# Creates a list of numbers from 1 to 10.
numList = [i for i in range(1,11)]
print(f"Original list: {numList}")

# Extracts the first five elements from the list.
first_five_elements_numList = numList[:5]
print(f"Extracted first five elements: {first_five_elements_numList}")

# Reverses these extracted elements.
reverse_first_five_numList = first_five_elements_numList[::-1]
print(f"Reversed extracted elements: {reverse_first_five_numList}")