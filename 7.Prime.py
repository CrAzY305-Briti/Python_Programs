def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False
    
    # Iterate over a range of numbers from 2 to n-1
    for i in range(2, n):
        # Check if n is divisible by the current number
        if n % i == 0:
            return False    
    # Return True if n is not divisible by any of the numbers in the range from 2 to n-1
    return True

n = int(input("Enter a number : "))
# Test the function
print(is_prime(n))
