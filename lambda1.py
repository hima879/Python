# Ask user to enter pairs separated by commas, e.g. "1 3,4 1,5 2"
user_input = input("Enter pairs of numbers separated by commas (e.g. 1 3,4 1,5 2): ")

# Convert input string into list of tuples of integers
# 1) Split input by commas to get each pair as a string
# 2) Strip spaces and split each pair by space to get numbers
# 3) Convert those number strings to integers, make a tuple
pairs = [tuple(map(int, pair.strip().split())) for pair in user_input.split(',')]

# Sorting using a regular function as key
def get_second(pair):
    return pair[1]

sorted_pairs = sorted(pairs, key=get_second)
print("Sorted pairs with regular function:", sorted_pairs)

# Sorting using a lambda function as key (does the same thing)
sorted_pairs_lambda = sorted(pairs, key=lambda pair: pair[1])
print("Sorted pairs with lambda function:", sorted_pairs_lambda)
