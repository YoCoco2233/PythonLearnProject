# 2024-7-25 23:53 start, 2024-7-25 23:58 end  @YoCoco2233 1-9-4 Nested For Loops

# Print a 3x3 grid of numbers
for i in range(3):  # Outer loop to control the rows
    for j in range(3):  # Inner loop to control the columns
        print(f"{i},{j}", end=" ")  # Print the current row and column indices, use end=" " to avoid a newline
    print()  # Print a newline after each row is printed
