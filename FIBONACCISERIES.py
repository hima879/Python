def fibonacci_series(n):
    # Initialize the first two Fibonacci numbers
    fib_series = [0, 1]

    # Generate Fibonacci numbers up to n terms
    for i in range(2, n):
        next_number = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_number)

    return fib_series

# Number of terms in the Fibonacci series
n = int(input("Enter the number of terms: "))  # User input for number of terms

# Check if the input is valid
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Get the Fibonacci series
    result = fibonacci_series(n)

    # Print the Fibonacci series
    print("Fibonacci series up to", n, "terms:")
    print(result)
