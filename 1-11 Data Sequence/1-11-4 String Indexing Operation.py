# 2024-8-9 22:45 start, 2024-8-9 23:31 end  @YoCoco2233 1-11-4  String Indexing Operation

# String indexing Operation in Python

# Define a string
string = "Hello, World!"

# indexing starts from 0 in Python,so the first character is at index 0
print(string[0])

# You can access any character in the string using its index
print(string[7])

# Negative indexing starts from the end of the string, -1 is the last character
print(string[-1])

# You can also use negative indexing to access characters from the end
print(string[-6])

# If you try to access an index that is out of the string's range, You'll get an IndexError
# print(string[20])

# String slicing allows you to access a range of characters using the starts and end indices
# Slicing syntax: String[start:end]
print(string[0:5])

# If you omit the start index, the slice starts from the beginning of the string
print(string[:5])

# If you omit the end index, the slice extends to the end of the string
print(string[7:])

# You can also use negative indices in slicing
print(string[-6:])