from functools import reduce  # 'reduce' is part of the functools module in Python

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# ------------------- MAP -------------------
# map(function, iterable): Applies the given function to each item in the iterable (e.g., list)
# Here, we define a named function to double each number

def double(x):
    return x * 2  # This function returns the input number multiplied by 2

# Apply 'double' to each element in 'numbers' using map
doubled = list(map(double, numbers))  # Converts the map object to a list
print("Doubled (using function):", doubled)
# Output: [2, 4, 6, 8, 10, 12]

# ------------------- FILTER -------------------
# filter(function, iterable): Filters elements from iterable where the function returns True
# Here, we use a lambda function to filter out only even numbers

evens = list(filter(lambda x: x % 2 == 0, doubled))  # Keep only numbers divisible by 2
print("Even numbers (using lambda):", evens)
# Output: [2, 4, 6, 8, 10, 12] (all are even in this case)

# ------------------- REDUCE -------------------
# reduce(function, iterable): Applies the function cumulatively to the items in the iterable
# Example: reduce(lambda x, y: x + y, [1, 2, 3]) → ((1 + 2) + 3) → 6
# Here, we multiply all the even numbers together

product = reduce(lambda x, y: x * y, evens)  # Multiplies all elements in 'evens'
print("Product of even numbers (using lambda + reduce):", product)
# Output: 46080
