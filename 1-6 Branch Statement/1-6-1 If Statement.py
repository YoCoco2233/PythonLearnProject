# 2024-7-11 16:10 start, 2024-7-11 16:34 end  @YoCoco2233 If Statement
# define age
age = 19
if age >= 18:
    print("You are a teenage.")
else:
    print("You are a kid")
# with  input(),need to type conversion..
age2 = int(input("Enter your age: "))
print(type(age2))
# >= not  comparison int and String
if age2 >= 18:
    print("You are a teenage.")
else:
    print("You are a kid")
age3= int(input("Enter your age: "))
if age3 < 18:
    print("You are a kid.")
elif age3 >= 18 and age3 < 25:
    print("You are a teenage.")
else:
    print("Your age is %s" % (age3))
