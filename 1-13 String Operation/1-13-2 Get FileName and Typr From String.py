#2024-8-20 19:24 start, 2024-8-20 19:54 end @YoCoco2233 1-13-2 Get File Name and Type From String
#Upload a file and get the filename and file type using Python
filename = input('Please enter the file name: ')

#The part before the last '.' is the filename, and the part after it is the file extension (type).
index = filename.rfind('.')
print('The file name is: ' + filename[:index]) # Here, index is the position of the last '.' from the left, slicing the string to get the filename before it.
print('The file type is: ' + filename[index:]) # Here, index is the position of the last '.' from the left, slicing the string to get the file extension after it.

#Check if the file name contains a '.'
if filename.rfind(".") != -1: # rfind() searches from the right, useful for files with multiple '.' like '123.tar.gz'
    print('This is a valid file.')
else:
    print('This is not a valid file.')
