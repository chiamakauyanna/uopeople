# Question 2: Write a Python code snippet that creates a tuple to store one borrower’s immutable personal details.
# Create a tuple, e.g., ("John Doe", "B1023", "2025-10-15") representing a borrower’s name, library ID, and membership date.
# Modify one element in the tuple, observe the result, and discuss your observation.
# Print the length of the tuple using the len() function to show how many data fields it contains and display each element using a loop.

borrower = ("Alex Smith", "B1023", "2025-10-15")
print(len(borrower))

for details in borrower:
  print(details)