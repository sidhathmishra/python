number1 = int(input("enter a number"))
operation = input("enter operation")
number2 = int(input("enter a number"))

#addition 
if "+"in operation:
    print(number1+number2)

#subtraction
elif "-"in operation:
    print(number1-number2)
#multiplication
elif "*"in operation:
    print(number1*number2)

#division
elif "/" in operation:
    print(number1/number2)

else:
    print("invalid operation")