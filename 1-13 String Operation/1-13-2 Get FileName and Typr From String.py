# 2024-8-20 19:24 start, 2024-8-20 19:54 end  @YoCoco2233 1-13-2 Get File Name and Type From String


# 上传文件，用Python获取文件名与文件类型

filename = input('请输入文件名称：')


# “.”点号左边的的文件名，点号右边的是文件类型。
index = filename.rfind('.')
print('文件名字是：' + filename[:index])# 这里index是从左往右数最后一个"."的位置，这里的意思是使用字符串的切片输出这个点号"."左侧的文件名称
print('文件类型是：' + filename[index:])# 这里index是从左往右数最后一个"."的位置，这里的意思是使用字符串的切片输出这个点号"."右侧侧的文件类型
#判断文件名称是否包含点号"."
if filename.rfind(".") != -1: # r+fid() = right find 从右边开始查询，考虑有多个"."的文件如123.tar.gz

    print('这是合理的文件')
else:
    print('不是合理的文件')


