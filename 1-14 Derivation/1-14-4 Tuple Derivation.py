# 2024-10-7 17:44 start, 2024-10-7 17:49 end  @YoCoco2233 1-14-4 Tuple derivation
"""
元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。

元组推导式基本格式：
(expression for item in Sequence)
或
(expression for item in Sequence  if  conditional)

元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来，而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。

例如，我们可以使用下面的代码生成一个包含数字 1~9 的元组：
"""
#实例
a = (x for x in range(1,10))
print(a)# 返回的是生成器对象
print(tuple(a)) # 使用 tuple() 函数，可以直接将生成器对象转换成元组