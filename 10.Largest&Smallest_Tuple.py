# Program to find largest / smallest number in a list
# # define a tuple of integers
# my_tuple = (3, 5, 2, 8, 1, 4)

# # use the max() function to find the maximum value in the tuple
# max_value = max(my_tuple)
# print("The maximum value in the tuple is:", max_value)

# # use the min() function to find the minimum value in the tuple
# min_value = min(my_tuple)
# print("The minimum value in the tuple is:", min_value)


# define a tuple of integers
my_tuple = (3, 5, 2, 8, 1, 4)

# sort the tuple in ascending order
sorted_tuple = sorted(my_tuple)

# the first element of the sorted tuple is the minimum value
min_value = sorted_tuple[0]
print("The minimum value in the tuple is:", min_value)

# sort the tuple in descending order
sorted_tuple = sorted(my_tuple, reverse=True)

# the first element of the sorted tuple is the maximum value
max_value = sorted_tuple[0]
print("The maximum value in the tuple is:", max_value)
