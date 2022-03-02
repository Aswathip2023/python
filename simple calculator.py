num1 = int(input("Enter a number"))
num2 = int(input("Enter next number"))
op = input("Enter operator")
if op == '+':
    sum = num1+num2
    print("Result =", sum)
elif op == '-':
    if num1 > num2:

        sub = num1-num2
        print("Result=", sub)

elif op == '*':
    mult = num1*num2
    print("Result=", mult)
elif op == '/':
    div = num1/num2
    print("Result=", div)


