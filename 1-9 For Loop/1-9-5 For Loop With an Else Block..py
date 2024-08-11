# 2024-7-27 19:43 start, 2024-7-27 19:56 end  @YoCoco2233 1-9-5 For Loop With an Else Block.

# Loop through a list of numbers and find number greater than 5.
# Use all features of the for loop, including the else block.

numbers = [2, 3, 5, 7, 11]
# Flag variable to indicate if we found a number greater than 5.
found = False

for number in numbers:
    # Check if the current number is greater than 5
    if number > 5:
        print(f"Found a number greater than 5: {number}")
        found = True
        # Exit the loop as we found the number.
        break
else:
    # This block is executed if the loop completes without encountering a break
    print("No numbers greater than 5 found in the list")

# Check the flag outside the loop to determine the outcome
if found:
    print("Loop completed due to a break.")
else:
    print("Loop completed normally.")