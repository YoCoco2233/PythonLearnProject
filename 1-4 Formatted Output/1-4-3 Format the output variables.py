# 2024-6-22 14:10 start, 2024-6-22 14:31 end  @YoCoco2233 Format the output variables

name = '元可可'
age = 19
# Limit int Number of digits and format
print('My name is %s, and I am %09d years old' % (name, age))

# Formatting of floating-point type variables
_title: str = 'price'
_value: float = 22.33
print('the %s is %f' % (_title, _value))
"""
the price is 22.330000
"""
# Keep 2 decimal places
print('the %s is %.2f' % (_title, _value))
"""
the price is 22.33
"""