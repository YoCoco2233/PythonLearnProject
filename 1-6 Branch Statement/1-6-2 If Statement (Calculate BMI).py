# 2024-7-12 17:49 start, 2024-7-12 16:59 end  @YoCocoium If Statement(Calculate BMI)
# BMI = kg / height**2
# Get height
height = float(input("Enter your height in m: "))
#  Get weight
weight = float(input("Enter your weight in kg: "))
# BMI  output
bmi = weight / (height * height)
print("Your BMI is", bmi)

if bmi >= 10 and bmi <= 18.4:
    print(f'Your BMI is: {bmi:2f}')
elif bmi >= 18.5 and bmi <= 24.9:
    print(f'Your BMI is: {bmi:2f}')
elif bmi >= 25 and bmi <= 27.9:
    print(f'Your BMI is: {bmi:2f}')
elif bmi >= 28 and bmi <= 39.9:
    print(f'Your BMI is: {bmi:2f}')