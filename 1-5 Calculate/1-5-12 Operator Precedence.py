# 2024-7-3 23:08 start, 2024-7-3 23:16 end  @YoCoco2233 Operator Precedence

# 括号 () 优先级最高
result1 = (3 + 4) * 2  # 结果为 14，不是 14 * 2 = 28，因为括号内的操作先执行

# 指数运算符 **
result2 = 2 ** 3 ** 2  # 结果为 512，不是 8 ** 2 = 64，因为 ** 是右结合的

# 正负号 +, -
result3 = -(3 + 4)  # 结果为 -7

# 乘法 *, 除法 /, 整除 //, 取模 %
result4 = 20 // 3 + 2 * 2  # 结果为 10，因为 // 和 * 优先级高于 +

# 加法 +, 减法 -
result5 = 10 - 3 - 2  # 结果为 5

# 位运算符 &, |, ^, ~, <<, >>（这里不展开所有，仅示例）
result6 = 4 << 2 | 1  # 结果为 17，因为 4 << 2 = 16, 16 | 1 = 17

# 比较运算符 <, <=, >, >=, ==, !=, is, is not, in, not in（这里不展开所有，仅示例）
# 注意：比较运算符的返回值是布尔值，这里仅作演示
result7 = 3 < 4 and 4 <= 5  # 结果为 True

# Assignment operators =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, <<=, >>=
# The assignment operator has the lowest precedence and is usually used at the end of the expression
# 赋值运算符 =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, <<=, >>=
# 赋值运算符的优先级是最低的，通常用于表达式的末尾
result8 = 0
result8 += 5  # 结果8，现在result8的值为5

# Logical operators not, and, or
# Note that the return value of a logical operator is a Boolean value or the value of the last evaluated expression
# 逻辑运算符 not, and, or
# 注意：逻辑运算符的返回值是布尔值或最后计算的表达式的值
result9 = not False and True or False  # result True

# Note: There are also some special operators in Python, such as the member operators in and not in, the identity
# operators is and is not, etc. They also have their own priority rules, but they are usually used for conditional
# judgment rather than numerical calculation. 注意：Python中还有一些特殊的运算符，如成员运算符in和not in，身份运算符is和is not等，
# 它们也有各自的优先级规则，但通常用于条件判断而不是数值计算。

print(f"result1: {result1}")
print(f"result2: {result2}")
print(f"result3: {result3}")
print(f"result4: {result4}")
print(f"result5: {result5}")
print(f"result6: {result6}")
print(f"result7: {result7}")
print(f"result8 after +=: {result8}")
print(f"result9: {result9}")
