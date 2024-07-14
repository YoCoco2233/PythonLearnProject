# 2024-6-23 18:22 start, 2024-6-23 18:35 end  @YoCocoium Swapping two values
"""
Swap the values of variables A and B
1,temporary variable
2,tuple unpacking
"""

# 1 Using a temporary variable
a = 5
b = 10
temp = a  # Store the value of a in a temporary variable
a = b  # Assign the value of b to a
b = temp  # Assign the temporary value(originally A's value to b)

# 2 Using tuple unpacking
_a = 5
_b = 10
_a, _b = _b, _a  # Swap the value of a and b using tuple unpacking
