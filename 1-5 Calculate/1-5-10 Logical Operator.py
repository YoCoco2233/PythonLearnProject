# 2024-7-2 23:08 start, 2024-7-2 23:15 end  @YoCoco2233 Comparison Logical Operator
a = 1
b = 2
c = 3

print((a > b) and (b > c))  # False
print((a > b) or (b > c))  # False
print((a < b) or (b > c))  # True
print(not (a > b))  # True

print(3 and 7 and 5)
print(5 and 6 or 7)
4 > 3 and print('Hello World')