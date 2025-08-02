# Decorator: a function that modifies another function's behavior.

def greet_decorator(func):  # 'func' is the original function to be decorated
    def wrapper():          # Wrapper adds extra behavior around 'func'
        print("Hello!")     # Before calling 'func'
        func()              # Call the original function
        print("Goodbye!")   # After calling 'func'
    return wrapper          # Return the new wrapped function

@greet_decorator           # Apply decorator to 'func'
def func():
    print("My name is Python.")  # Original function logic

func()  # Calls the wrapped function
# Output:
# Hello!
# My name is Python.
# Goodbye!
