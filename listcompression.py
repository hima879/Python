numbers = [1, 2, 3, 4, 5]  # Original list of numbers

# 1. Double the numbers using list comprehension
# For each number i in numbers, multiply it by 2 and collect the results in a new list
doubled = [i * 2 for i in numbers] 

# 2. Get only even numbers using list comprehension with a condition
# For each number i in numbers, include it in the new list only if i is divisible by 2 (even)
evens = [i for i in numbers if i % 2 == 0]

# 3. Square each number using list comprehension
# For each number i in numbers, compute i squared (i**2) and collect in a new list
squares = [i ** 2 for i in numbers]

# 4. Triple each number using lambda and map function
# map applies the lambda function (which triples the input) to every element in numbers,
# then list() converts the map object to a list
tripled = list(map(lambda x: x * 3, numbers))

# Print the results
print("Original:", numbers)
print("Doubled:", doubled)
print("Evens:", evens)
print("Squares:", squares)
print("Tripled:", tripled)
