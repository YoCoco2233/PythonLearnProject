# 2024-6-23 18:43 start, 2024-6-23 18:35 end  @YoCoco2233 Type Casting

# Product name
name = input('Enter the product name: ')
# Quantity of the product
number = input('Enter the quantity of the product: ')
# Price of the product
price = input('Enter the price of the product: ')

# Format Output
print(f'You purchased product {name}, the quantity is {number}, at a price of {price * 2}')
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
            - Converts the Python expression in the string str and returns an object
 
"""