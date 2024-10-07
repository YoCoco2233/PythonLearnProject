# 2024-10-7 17:34 start, 2024-10-7 17:41 end  @YoCoco2233 1-14-3 Set derivation
"""集合推导式基本格式：

{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
"""
#计算数字1,2,3的平方数
setnew = {i**2 for i in (1,2,3)}
print(setnew)

#判断不是abc的字母并输出(区分大小写)
a = {x for x in 'YoCoco' if x not in '2233'}
print(a)
print(type(a))