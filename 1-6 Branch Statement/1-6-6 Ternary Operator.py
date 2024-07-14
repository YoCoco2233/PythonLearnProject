# 2024-7-14 23:50 start, 2024-7-14 23:57 end  @YoCocoium Ternary Operator
# a concise way to choose one of two values based on a condition being true or false.
condition = True
x = 0
y = 1
print(x if condition else y)
condition = False
x = 0
y = 1
print(x if condition else y)

age = 19
is_adult = "Yes" if age >= 18 else "No"
print(is_adult)

age2 = 15
category = "Child" if age2  < 13 else "Teenage"
print(category)