# 2024-6-23 18:43 start, 2024-6-23 18:35 end  @YoCoco2233 Type Casting

# Product name
name = input('Enter the product name: ')
# Quantity of the product
number = input('Enter the quantity of the product: ')
# Price of the product
price = input('Enter the price of the product: ')

# Format Output
print(f'You purchased product {name}, the quantity is {number}, at a price of {price * 2}')
print(f'You purchased product {name}, the quantity is {number}, at a price of {eval(price) * 2}')
"""
The string 'price' is of string type and cannot participate 
in normal mathematical calculations 
"""
# 'price' need to convert to a numeric type
"""
1, int(x [,base]): Function description 
                - converts x to an integer.optionally,base 
                specifies the base for the conversion.  

2, float(x): Function description 
            - converts x to a floating-point number
            
3, complex(real [,imag]): Function description 
                        - creates a complex number with real as the real
                        part and imag as the imaginary part(default to 0 if provided)  

4, str(x): Function description
        - Converts object x to a string
        
5, repr(x): Function description
            - Converts the Python expression in the string str and returns an object x
            ro a string representation suitable fro debugging and display.
            
6, eval(str)：Function description
            - evaluates the Python expression in the string str and returns an object.
            
7, tuple(s)：Function description
            - converts the sequence s to a tuple.
            
8, list(s)：Function description
            - converts the sequence s to a list.
            
9, chr(x)：Function description
            - converts an integer x to a Unicode character.
            
10, ord(x)：Function description
            - converts a character x to its ASCII integer value.
            
11, hex(x)：Function description
            - converts an integer x to a hexadecimal string.
            
12, oct(x)：Function description
            - converts an integer x to an octal string.
            
13, bin(x)：Function description
            - converts an integer x to a binary string.
            
"""

num = input('Please input you luck number')
print(type(num))
num = int(num)
print(type(num))
"""
<class 'str'>
<class 'int'>
"""

num1 = 10
print(type(num1))
print('-' * 10)
num1 = float(num1)
print(type(num1))

# float to int ,loss float value
num2 = 22.33
print(type(num2))
print('-' * 10)
num2 = int(num2)
print(num2)
print(type(num2))

str1 = '2233'
str2 = 22.33
num1 = int(str1)
num2 = float(str2)
print(type(str1))
print(type(str2))


