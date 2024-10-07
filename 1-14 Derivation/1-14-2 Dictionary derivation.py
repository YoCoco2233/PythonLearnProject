# 2024-10-7 17:18 start, 2024-10-7 17:32 end  @YoCoco2233 1-14-2 Dictionary derivation
"""字典推导基本格式：

{ key_expr: value_expr for value in collection }

或

{ key_expr: value_expr for value in collection if condition }
使用字符串及其长度创建字典：
"""
#实例
listdemo = ['A1','A2', 'A3']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)


#提供三个数字，以三个数字为键，三个数字的平方为值来创建字典：

#实例
dic = {x: x**2 for x in (2, 4, 6)}
print(dic)

print(type(dic))
