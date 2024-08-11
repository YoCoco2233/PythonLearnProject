# 2024-7-18 22:11 start, 2024-7-18 22:38 end  @YoCoco2233 Break and Continue
# to initialize a counter
counter = 0

# While loop that will run until counter reaches 10
while counter < 10:
    counter += 1  # increment the counter

    # Use continue to skip the rest of the loop and continue to the next interation
    if counter == 5:
        print("Skipping counter value 5")
        continue

    # Some continue to break the loop , let's say when counter is 8.
    if counter == 8:
        print("Breaking the loop at  counter value 8")
        break
print("Counter value was: ", counter)
# output will show counter values from 1 to 9, skipping 5 and breaking at 8.
