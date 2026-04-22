# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
# Task 1:
# Declare an empty list called inventory to store item names as strings.

# Add your code here

    # Declare an empty list called "inventory" to store items names
inventory = []

# Task 2:
# Write a function called addItem(itemName) that adds the given item to the
# inventory list. If the item already exists, print a message instead of adding it.
# Example message: "Mouse is already in inventory."


def addItem(itemName):
    # Add your code here
    # If the itemName is already in the inventory list, then it will print a message indicating item is already in inventory.
    # Otherwise, it will add the itemName to the inventory list using the append() method to add into the end of the existing list.
   if itemName in inventory:
        print(f"{itemName} is already in inventory.")
   else:
        inventory.append(itemName)
   
# Task 3:
# Write a function called listInventory() that prints all items in the inventory.
# If the inventory is empty, print: "Inventory is empty."

   # Define a function called listInventory that prints the items in the inventory list
def listInventory():
    # Add your code here
    # Check if the lenght of inventory list is 0, if it is empty then it will print "Inventory is empty."
    # Otherwise, it will print the current items in the inventory list.
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Inventory:", inventory)
        
# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
