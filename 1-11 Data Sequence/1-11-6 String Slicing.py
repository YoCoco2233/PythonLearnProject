# 2024-8-12 21:40 start, 2024-8-12 21:46 end  @YoCoco2233 1-11-6 String Slicing

# Define a sample string
sample_string = "Python is fun to Learn!"

# Slicing the String to get the first 5 characters
# This shows basic slicing syntax
print("First 5 characters:", sample_string[0:5])

# Slicing the string from the 6th character to the end
# Note that the stop index is omitted, which means slice until the end
print("From 6th character to the end:", sample_string[6:])

# Using negative indices to slice from the end
# This gets the last 5 characters of the string
print("Last 5 characters:", sample_string[-5:])

# Slicing with a step size
# This gets every third character from the string
print("Every third character:", sample_string[::3])

# Reverse slicing
# This reverses the entire string by specifying a negative step size
print("Reversed string:", sample_string[::-1])

# Note: String slicing does not modify the original string
# It crea a new string with the specified slice of the original
print("Original string remains:", sample_string)
