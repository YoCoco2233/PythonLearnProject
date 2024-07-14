# 2024-6-26 18:28 start, 2024-6-26 18:35 end  @YoCocoium eal function
# eval primarily used for type conversion operations in strings
str1 = '22'
str2 = '22.33'

num1 = eval(str1)
print(type(num1))

num2 = eval(str2)
print(type(num2))


"""
<class 'int'>
<class 'float'>
"""