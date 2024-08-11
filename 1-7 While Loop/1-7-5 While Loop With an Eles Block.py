# 2024-7-26 21:03 start, 2024-7-26 21:09 end  @YoCoco2233 1-7-5 While Loop With an Else Block.

# Example of a while loop with an else block

# Initialize the counter
counter = 0

# Loop until counter is greater than 3
while counter < 3:
    print(f'Counter is: {counter}')
    # Increment the counter.
    counter += 1
else:
    # This else block is executed when the loop finishes normally.
    print('The loop has finished normally.')

# If we had a break statement inside the loop, the else block would not execute.
