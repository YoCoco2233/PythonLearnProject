# 2024-7-21 22:15 start, 2024-7-21 22:26 end  @YoCoco2233 Print Right Triangle

# Define the height of the triangle.
height = 10

# Define loop for rows.
row = 1

while row <= height:
    # Inner loop for columns
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    # move to the next line after printing each row.
    print()
    row += 1

