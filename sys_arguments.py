import sys          # Provides access to command-line arguments and system functions
import os           # Helps with handling file and directory paths

# Extract just the script's filename without the full directory path
# sys.argv[0] is the full path (or just filename) of the script being run
script_name = os.path.basename(sys.argv[0])

# Initialize the args list starting with the script filename itself
args = [script_name]

# Append any additional command-line arguments passed to the script (if any)
# sys.argv[1:] contains all arguments after the script name
args += sys.argv[1:]

# Check if no arguments were passed besides the script name
if len(args) == 1:
    # If true, prompt the user to enter some arguments manually
    # The user can type multiple arguments separated by spaces
    user_input = input("No arguments provided. Please enter some arguments separated by spaces: ")
    
    # Split the input string by spaces to convert into a list of arguments
    # Then append those user-provided arguments to the args list
    args += user_input.split()

# Print all arguments including the script name
print("Stored arguments:", args)

# Print the first argument after the script name (if any)
if len(args) > 1:
    print("First argument:", args[1])
else:
    print("No arguments provided.")

# Print the total count of arguments including the script name
print("Number of arguments provided (including script name):", len(args))

# Print the count of arguments excluding the script name
print("Number of arguments provided (excluding script name):", len(args) - 1)

