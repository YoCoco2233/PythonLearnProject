# 2024-8-13 19:01 start, 2024-8-13 19:46 end  @YoCoco2233 1-12-1 Operating Methods for Files

# 定义文件路径
file_path = 'example.txt'

# 打开文件读取内容，如果文件不存在则报错
# 使用‘with’语句可以自动管理文件的打开和关闭
with open(file_path, 'r') as file:  # 'r'表示读取模式
    # 读取文件全部内容
    content = file.read()
    print("文件内容：")
    print(content)

# 打开文件以写入内容，如果文件不存在则创建
# 注意：这会覆盖文件原有内容
with open(file_path, 'w') as file:  # 'w'表示写入模式
    # 写入内容到文件
    file.write("Hello YoCoco, This is a new content:\n")
    file.write("Writing to files is easy in Python")

# 打开文件以追加内容
# 如果文件不存在，则创建文件
with open(file_path, 'a') as file:  # 'a'表示追加模式
    # 追加内容到文件
    file.write("\n加入更多内容：")

# 注意,在实际使用中,'with'语句确保了文件在操作完成后会被正常关闭。
# 无需显式调用file.close()

# 如果需要读取文件的每一行，可以使用for循环
with open(file_path, 'r') as file:
    for line in file:  # 逐行读取
        print(line, end='')  # 打印每行，end=''避免打印额外的换行符

