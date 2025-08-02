def calculator(): 
    # Read the first number 
    num1 = float(input("Enter the first number: "))

    # Read the operation
    operation = input("Enter the operation (+, -, *, /): ")  

    # Read the second number
    num2 = float(input("Enter the second number: "))

    # Perform the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            calculator()  # Restart the calculator if there's an error
            return
    else:
        print("Invalid operation!")
        calculator()  # Restart the calculator if the operation is invalid
        return

    # Print the result
    print(f"The result of {num1} {operation} {num2} is {result}")

    # Ask if the user wants to perform another calculation
    another = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another == 'yes':
        calculator()  # Recursive call to restart the calculator
    else:
        print("Goodbye!")

# Start the calculator
calculator()

