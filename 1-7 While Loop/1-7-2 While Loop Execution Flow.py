# 2024-7-17 23:51 start, 2024-7-17 23:58 end  @YoCocoium While Loop Execution Flow
# Initialize a counter variable
counter = 0
# Set a limit for the counter
limit = 10
while counter < limit:
    # increment the counter
    counter += 1

    # print the current counter value
    print(f"Current counter value:{counter}")

    # if the counter reaches a certain value,print a special message
    if counter % 2 == 5:
        print(f"Current counter value:{counter}")

# code outside the loop while execute after the loop terminates
print(f"Loop has ended. ")
