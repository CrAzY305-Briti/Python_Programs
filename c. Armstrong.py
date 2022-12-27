# Program to determine Armstrong number
def is_armstrong(num):
  # Convert the number to a string and get the length
  num_str = str(num)
  len_num = len(num_str)

  # Initialize a variable to store the sum of the digits raised to the power of the length
  sum = 0

  # Iterate through each digit in the number
  for digit in num_str:
    # Convert the digit to an integer and add it to the sum after raising it to the power of the length
    sum += int(digit) ** len_num
  # Return True if the sum is equal to the original number, False otherwise
  return sum == num

num = int(input("Enter a number : "))

# Test the function 
print(is_armstrong(num))
