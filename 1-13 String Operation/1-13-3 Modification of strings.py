#2024-8-24 19:24 start, 2024-8-24 21:54 end @YoCoco2233 1-13-3 Modification of String

# 修改字符串，就是通过函数的形式修改字符串中的数据
"""
replace():返回替换后的字符串
split():返回切割后的字符串序列
join():用一个字符或子串合并字符串，即是将多个字符合并为一个新的字符串
upper():与lower():返回全部大写或全部小写的字符串
"""

str1 = 'hello linux'
str2 = str1.replace('linux','python')
print(str2)

str1 = 'hello linux, hello linux'
str2 = str1.replace('linux','python',1)
print(str2)


str1 = 'apple-banana-orange'
print(str1.split('-'))
str3 = ['apple','bnana','orange']
print('+'.join(str3))

username = input('UserName')
password = input('Password')

if username.lower() == 'yococo' and password.lower() == 2233:
    print('welcome YoCoco')
else:
    print('Please try again')