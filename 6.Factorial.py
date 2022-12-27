# # Get the number from the user
# n = int(input("Enter a number: "))

# # Initialize the result to 1
# result = 1

# # Calculate the factorial
# for i in range(1, n+1):
#     result *= i

# # Print the result
# print("The factorial of", n, "is", result)

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

num = int(input("Enter a number : "))
print(factorial(num))
