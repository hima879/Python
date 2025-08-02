# Regular function that adds 2 to a number
def add_two(x):
    return x + 2

print(add_two(5))  # Output: 7

"""A lambda function is a small, anonymous function (a function without a name).
It can take any number of arguments but only has one expression.
The result of that expression is automatically returned.
Useful for quick, short functions without formally defining them using def."""
# Equivalent lambda function that adds 2 to a number
add_two_lambda = lambda x: x + 2

print(add_two_lambda(5))  # Output: 7 
