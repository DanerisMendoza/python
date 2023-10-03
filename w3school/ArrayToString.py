# Example array of integers
# number_array = [1, 2, 3, 4, 5]

# # Convert integers to strings using list comprehension
# string_array = [str(num) for num in number_array]

# # Using the join method to concatenate the strings with a comma separator
# result_string = ', '.join(string_array)

# # Print the result
# print(result_string)

# 2nd method 
number_array = [1, 2, 3, 4, 5]
result_string = ''.join(map(str, number_array))
# result_string = (map(str, number_array))
print(result_string)