num1 = int(input("Enter a number"))
num2 = int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))
if (num1>num2) and (num1>num3):
    print("biggest number is",num1)
elif (num2>num1 and num2>num3):
    print("biggest number is",num2)
else:
    print("biggest number is",num3)