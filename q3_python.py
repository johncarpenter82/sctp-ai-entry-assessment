# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    # Add your code here
    
    # Capitalize first letter, rest lowercase
    first = firstName.capitalize()
    last = lastName.capitalize()
    
    # Return formatted string in the format "lastName, firstName" with first letter of each name capitalized and the rest in lowercase
    # Separate the last name and first name with a comma and a space
    return f"{last}, {first}"
   

# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    # Add your code here
    # Take first character [0] of the string and convert it to uppercase using .upper() method
    first_initial = firstName[0].upper()
    last_initial = lastName[0].upper()

    # Return the initials in the format "F.L." where F is the uppercase first initial and L is the uppercase last initial, 
    # Separated by a "." and followed by another "." at the end
    return f"{first_initial}.{last_initial}."


# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

# Add your code here

    # Print the results of calling formatName and formatInitials functions with the specified inputs
print(formatName("Alice", "Tan"))   # Expected: "Tan, Alice"
print(formatName("bob", "lim"))     # Expected: "Lim, Bob"
print(formatInitials("Alice","Tan")) # Expected: "A.T."
print(formatInitials("bob","lim"))   # Expected: "B.L."