# 2024-8-13 19:01 start, 2024-8-13 19:46 end  @YoCoco2233 1-12-1 Operating Methods for Files

# Define file path
file_path = 'example.txt'

# Open the file to read content, if the file does not exist, an error will be raised
# Using the 'with' statement can automatically manage the opening and closing of the file
with open(file_path, 'r') as file:  # 'r' represents read mode
    # Read the entire content of the file
    content = file.read()
    print("File content:")
    print(content)

# Open the file to write content, if the file does not exist, it will be created
# Note: This will overwrite the existing content of the file
with open(file_path, 'w') as file:  # 'w' represents write mode
    # Write content to the file
    file.write("Hello YoCoco, This is a new content:\n")
    file.write("Writing to files is easy in Python")

# Open the file to append content
# If the file does not exist, it will be created
with open(file_path, 'a') as file:  # 'a' represents append mode
    # Append content to the file
    file.write("\nAdding more content:")

# Note, in practical use, the 'with' statement ensures that the file will be properly closed after the operation.
# There is no need to explicitly call file.close()

# If you need to read each line of the file, you can use a for loop
with open(file_path, 'r') as file:
    for line in file:  # Read line by line
        print(line, end='')  # Print each line, end='' avoids printing an additional newline character
