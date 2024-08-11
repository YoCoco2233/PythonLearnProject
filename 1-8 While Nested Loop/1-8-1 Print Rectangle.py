# 2024-7-20 19:37 start, 2024-7-20 20:14 end  @YoCoco2233 Print Rectangle

# Method 1: Basic Nested Loop
print("Method 1: Basic Nested Loop")
i = 0 # Initialize the outer loop counter.
while i < 22: # outer loop for rows
    j = 0 # initialize the inner loop counter.
    while j < 33:
        print(i, j, end=' ')
        j += 1
    print() # Print a new line after each row.
    i += 1

# Method 2: Using List Comprehension
print("Method 2: Using List Comprehension")
i = 0
while i < 22:
    print(''.join(['*' for _ in range(33)])) # Print row of 33 asterisks.
    i += 1
# Method 3: Using String Multiplication
i = 0
while i < 22:
    print('*' * 33)  # Print a row of 33 asterisks using string multiplication
    i += 1
# Method 4: Printing the Entire Rectangle as a Single String
rectangle = ('*' * 33 + '\n') * 22  # Create the rectangle as a multi-line string
print(rectangle, end='')
# Method 5: Nesting a while loop inside a for loop (Variant Example)
for i in range(22):  # Use a for loop for the rows
    j = 0
    while j < 33:  # Use a while loop for the columns
        print('*', end='')
        j += 1
    print()

