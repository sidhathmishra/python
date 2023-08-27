number = int(input("enter a number>>>"))
if number > 0:# every positive integer is bigger than 0
    flag = True
    print(number*number)
elif number < 0:#every negative number is smaller than 0
    flag = True
    print(number*number*number)
else:
    pass