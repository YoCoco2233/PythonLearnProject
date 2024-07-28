# 2024-7-28 23:49 start, 2024-7-28 23:56 end  @YoCoco2233 1-10-1 For Loop Case 1

nums = int(input('input: '))
count = 0
for i in range(1, nums+1):
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        continue
    count = count + 1
print(f'There are {count} even numbers.')