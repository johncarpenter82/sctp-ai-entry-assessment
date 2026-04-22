# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

    # Create a function called convertTemp, which receives a temperature value and its unit (C or F)
def convertTemp(value, unit): 
     # Add your code here
     # Check the type of variable value if it integer or decimal value, if not belong to these types return -1
    if not isinstance(value, (int, float)):
        return -1
    
    # Convert unit to uppercase, so that it can handle both lowercase and uppercase inputs, .upper() method is to convert the unit to upper case
    unit = unit.upper()
    
    # if the received unit is "C" - after the upper case conversion, then it will multiply the value by 9/5 and add 32 to convert it to Fahrenheit
    if unit == "C":
        result = (value * 9/5) + 32
    # if the received unit is "F" - after the upper case conversion, then it will subtract 32 from the value and multiply by 5/9 to convert it to Celsius
    elif unit == "F":
        result = (value - 32) * 5/9
    # if the unit is neither "C" nor "F", it will return -1 to indicate an invalid unit
    else:
        return -1
    # Finally, it will round the result to 2 decimal places using the round() function and return it
    return round(result, 2)
    
   
# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

# Add your code here
# Call the convertTemp function with the specified inputs and print the results
print(convertTemp(100, "C"))      # Expected: 212.0
print(convertTemp(32, "F"))       # Expected: 0.0
print(convertTemp(37, "C"))       # Expected: 98.6
print(convertTemp("invalid","X")) # Expected: -1