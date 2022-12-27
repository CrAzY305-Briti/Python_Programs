# Program to determine Palindrome number
def is_palindrome(num):
  # Convert the number to a string
  num_str = str(num)

  # Reverse the string
  rev_str = num_str[::-1]

  # Compare the reversed string to the original string
  if rev_str == num_str:
    return True
  else:
    return False

num = int(input("Enter a number : "))
# Test the function
print(is_palindrome(num))
