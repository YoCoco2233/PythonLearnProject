# 2024-7-23 22:46 start, 2024-7-23 22:52 end  @YoCoco22331-9-2 Calculate the sum number from 1 to 100.

# Calculate the sum of all even numbers from 1 to 100

# Initialize a variable to store the sum of even numbers
sum_of_evens = 0

# Loop through all numbers from 1 to 100
for number in range(1, 101):
    # Check if the number is even
    if number % 2 == 0:
        # If the number is even, add it to the sum
        sum_of_evens += number

# Print the result
print("The sum of all even numbers from 1 to 100 is:", sum_of_evens)
