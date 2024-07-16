# 2024-6-20 00:15 start, 2024-6-20 4:00 end  @YoCoco2233 DataType
"""
    Vi har alle tvil, Spørsmål om valg, Er dette det du vil
    (对于选择,我们心存疑虑,这是你要的结果吗?)
"""
"""
1,Basic Data Types
integer,Float,Character,Boolean
"""
#int
intnumber: int = 1
print(type(intnumber))
# float
_float_number: float = 0.0
print(type(_float_number))
# bool(True/False) Must be Capitalized
_Bool_Object: bool = True
print(type(_Bool_Object))
# string(str)
_String_Object: str = "String"
print(type(_String_Object))

# Check if a variable is of a special type
print(isinstance(_String_Object, str))
print(isinstance(_float_number, bool))
"""
2,Container Types
Array,List[1,2,2,3,3],Tuple(1,2,3),Set{1,2,3},dictionary{key:value}
"""
import array

# create int array,创建一个包含整数的数组
_int_array = array.array('i', [1, 2, 3, 4, 5])
print(_int_array)  # output

# Access the element in an array,访问数组中的元素
print(_int_array[2])

# Modify an element in sn array,修改数组中的元素
_int_array[2] = 10
print(_int_array)

# Add a new element to the end of an array,添加新元素到数组的末尾
_int_array.append(6)
print(_int_array)

# Convert an array to a List,将数组转换为列表
_list_version = _int_array.tolist()
print(_list_version)

# List
_List: list = [1, 2, 3, 4, 5, 6]
print(_List)
print(type(_List))

# Tuple
_Tuple: tuple = (1, 2, 3, 4, 5, 6)
print(_Tuple)
print(type(_Tuple))

# set
_set: set = {1, 1, 3, 4, 5, 6}
print(_set)
print(type(_set))

# Dictionary
_Dictionary = {'Name': '元可可', 'age': 19}
print(_Dictionary)
print(type(_Dictionary))