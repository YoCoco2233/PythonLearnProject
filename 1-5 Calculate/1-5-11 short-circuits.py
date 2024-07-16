# 2024-7-2 23:25 start, 2024-7-2 23:50 end  @YoCoco2233 short-circuits
"""
The expression returns the value of the operand that determines the over result

"""
print(3 and 7 and 5)  # 5
print(3 and 0 and 5)  # 0
print(0 and 7 and 5)  # 0

print(5 and 6 or 7)
4 > 3 and print('Hello World')

"""
(0,null,'',none) == False 
(numerical vale and string(not empty) ) == True

"""
print(3 and 4)  # 4
print(0 and 1)  # 0

str1 = ''
num1 = 5
print(str1 and num1)  # ''

str2 = ' '
print(str2 and num1)  # 5

print(6 or 7)  # 6
