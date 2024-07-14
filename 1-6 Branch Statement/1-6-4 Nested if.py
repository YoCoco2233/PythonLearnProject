# 2024-7-13 20:15 start, 2024-7-13 21:15 end  @YoCocoium Nested If
# A nested is when you have an if statement inside another if statement
proof = int(input("Please input the alcohol content (mg) per 100 milliliters of blood: "))
if proof < 20:
    print("Your alcohol content is below 20mg", proof)
else:
    if 80 > proof >= 20 :
        print("Your alcohol content is above 20mg", proof)
    else:
        print("Your alcohol content is  80mg", proof)