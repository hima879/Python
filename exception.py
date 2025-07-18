# Define a function to check if someone can enter the club
def enter_club(age):
    # Check if the person is younger than 18
    if age < 18:
        # If they are too young, raise an error
        raise Exception("You're too young to enter!")
    # If the age is 18 or older, welcome them
    print("Welcome to the club!")

# Try to run the function and catch any errors
try:
    # Ask the user to enter their age and convert it to an integer
    user_age = int(input("Enter your age: "))
    
    # Call the function with the user's age
    enter_club(user_age)

# Catch and handle the exception if raised
except Exception as e:
    # Print the error message
    print("Error:", e)
