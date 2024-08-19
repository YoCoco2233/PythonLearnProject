# 2024-8-19 21:02 start, 2024-8-19 21:21 end  @YoCoco2233 1-13-1 String Search

# 字符串变量.find(要搜索的内容) 检查某个子串是否包含在这个字符串中，如果在，返回这个字串开始的位置下标，否则返回-1.

# 字符串变量.index(要搜索的内容) 检查某个子串是否包含在这个字符串中，若果在，返回这个字串开始的位置下标，否则报异常。

str1 = 'hello world'
print(str1.find('linux'))
print(str1.find('world'))

str2 = 'Hello Python'
print(str1.find('Python'))
print(str2.index('Python'))


#print(str2.index('Linux'))

"""
判断输入文件名称点号的位置，如上传功能
"""
filename = input('请输入文件完整名称：')
if filename.find('.') > -1:
    print('点号存在')
else:
    print('点号不存在')