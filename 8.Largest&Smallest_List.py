# Program to find largest / smallest number in a list
# # define a list of integers
# my_list = [3, 5, 2, 8, 1, 4]

# # use the max() function to find the largest value in the list
# max_value = max(my_list)
# print("The largest value in the list is:", max_value)

# # use the min() function to find the smallest value in the list
# min_value = min(my_list)
# print("The smallest value in the list is:", min_value)

# define a list of integers
my_list = [3, 5, 2, 8, 1, 4]

# sort the list in ascending order
sorted_list = sorted(my_list)

# the first element of the sorted list is the smallest value
min_value = sorted_list[0]
print("The smallest value in the list is:", min_value)

# sort the list in descending order
sorted_list = sorted(my_list, reverse=True)

# the first element of the sorted list is the largest value
max_value = sorted_list[0]
print("The largest value in the list is:", max_value)
