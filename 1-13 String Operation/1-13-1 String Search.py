# 2024-8-19 21:02 start, 2024-8-19 21:21 end @YoCoco2233 1-13-1 String Search

# The .find(substring) method of a string variable checks if a substring is present within the string. If it is, it returns the starting index of the substring; otherwise, it returns -1.
# The .index(substring) method of a string variable also checks if a substring is present within the string. If it is, it returns the starting index of the substring; otherwise, it raises an exception.
str1 = 'hello world'
print(str1.find('linux')) # This will print -1 because 'linux' is not found in str1.
print(str1.find('world')) # This will print the index where 'world' starts in str1.

str2 = 'Hello Python'
print(str1.find('Python')) # This will print -1 because 'Python' is not found in str1.
print(str2.index('Python')) # This will print the index where 'Python' starts in str2.

# Uncommenting the following line will raise an exception if 'Linux' is not found in str2.
#print(str2.index('Linux'))
"""
Determine the position of the dot in the input file name, e.g., for an upload function.
"""
filename = input('请输入文件完整名称：')
if filename.find('.') > -1:
    print('点号存在')
else:
    print('点号不存在')