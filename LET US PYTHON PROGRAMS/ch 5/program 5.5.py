# suppose ther are four flag variables variables w , x , y , z.Write a program to check in multiple ways whether one of them true.

w , x , y , z = 0,1,0,1
#1st way
if w == 1 and x == 1 and y == 1 and z == 1:
    print("True")
#2nd way
if any((w==1,x==1,y==1,z==1)):
    print("True")
else:
    print("False")