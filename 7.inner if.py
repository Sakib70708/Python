"""
highest number cheak
"""
num1=float(input("Enter the 1st number: "))
num2=float(input("Enter the 2nd number: "))
num3=float(input("Enter the 3rd number: "))
if num1>num2:
    if num1>num3:
        print(num1,"  is higher")
    else:
        print(num3," is higher")
if num2>num3:
    if num2>num1:
        print(num2," is Higher")
if num3>num1:
    if num3>num2:
        print(num3," is higher")

