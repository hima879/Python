import argparse  # Import the argparse module to handle command-line arguments

# Description message to explain what the program does
description = "A simple CLI tool to manage your tasks."

# Create an ArgumentParser object with the description
parser = argparse.ArgumentParser(description=description)

# Define a command-line argument "-c" or "--color" to accept a color input from the user
# The help message describes what this argument is for
parser.add_argument("-c", "--color", help="The color to search for")

# Parse the arguments passed from the command line and store them in 'args'
args = parser.parse_args()

# Check if the user did NOT provide a color argument, or if it's empty/only spaces
if not args.color or args.color.strip() == "":
    # If no valid color was provided, print the description to inform the user about the program
    print("\n" + description + "\n")
    
    # Then prompt the user to manually enter the color via input()
    # .strip() removes any leading or trailing spaces from the input
    args.color = input("Enter the color to search for: ").strip()

# Finally, print the color that was either provided via command-line or input by the user
print("You entered color:", args.color)
 