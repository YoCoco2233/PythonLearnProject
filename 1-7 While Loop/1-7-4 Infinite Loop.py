# 2024-7-19 18:06 start, 2024-7-19 18:14 end  @YoCoco2233 Infinite Loop

# Be careful , as this loop will never stop interrupted manually!
max_iterations = 10
iterations = 0

while True:
    if iterations < max_iterations:
        iterations += 1
        print('This loop will runforever !')
    if iterations == max_iterations:
        break


