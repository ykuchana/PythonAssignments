"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

write_text = input("Enter text to write to the file: ")
file_name = "output.txt"

with open(file_name, "wt") as fh:
    fh.write(write_text)
    print(f"Data successfully written to {file_name}.")

print()
append_text = "\n"+input("Enter additional text to append: ")
with open(file_name, "at") as afh:
    afh.write(append_text)
    print(f"Data successfully appended.")

print()
print(f"Final content of {file_name}:")
with open(file_name, "rt") as rfh:
    data = rfh.readlines()
    for dt in data:
        print(dt.rstrip("\n"))
# print(data)