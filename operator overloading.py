# Define a class called Box to represent a real-world storage box
class Box:
    # This is the constructor method; it runs when you create a new Box
    def __init__(self, owner, items):
        self.owner = owner        # Store the name of the box owner
        self.items = items        # Store a list of items inside the box

    # Operator overloading for '+' — defines how to combine two boxes
    def __add__(self, other):
        # Create a new combined owner name (e.g. "Alex & Maya")
        combined_owner = f"{self.owner} & {other.owner}"
        # Merge the item lists from both boxes
        combined_items = self.items + other.items
        # Return a new Box with the combined owner and items
        return Box(combined_owner, combined_items)

    # This method defines how the Box will look when printed using print()
    def __str__(self):
        # Return a nicely formatted string that shows owner and items
        return f"📦 Box for {self.owner} contains: {self.items}"

# -------------------------------
# Now let's use the Box class
# -------------------------------

# Create a box owned by Alex with some items
alex_box = Box("Alex", ["books", "shoes"])

# Create a box owned by Maya with her items
maya_box = Box("Maya", ["toys", "clothes"])

# Combine both boxes using the overloaded '+' operator
# This creates a new box with both owners and all items
shared_box = alex_box + maya_box

# Print details of each box

# Prints: 📦 Box for Alex contains: ['books', 'shoes']
print(alex_box)

# Prints: 📦 Box for Maya contains: ['toys', 'clothes']
print(maya_box)

# Prints: 📦 Box for Alex & Maya contains: ['books', 'shoes', 'toys', 'clothes']
# This is the result of operator overloading
print(shared_box)
