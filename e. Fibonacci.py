# def print_fibonacci_series(n):
#   a, b = 0, 1
#   while a < n:
#     print(a, end=' ')
#     a, b = b, a+b

# a = int(input("Enter a number : "))
# print_fibonacci_series(a)

# Program to display the terms of a Fibonacci series
def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n == 0 or n == 1:
        return n
    # Recursive case: return the sum of the previous two terms
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# Print the first n terms of the series
for i in range(n):
  print(fibonacci(i))
