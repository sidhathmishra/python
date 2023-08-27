#use of and
a = 40
b = 30
x = 75 and a >= 20 and b < 60 and 35 #and returns last expression(left to right) if all conditions are true
print(x) #returns 35
#use of or
a = 40
b = 20
x = 75 or a >= 20 or 60#or returns any condition which is true 
y = a >= 20 or 75 or 60#or returns any condition which is true 
z = a < 20 or 0 or 35#or returns any condition which is true 
print(x)#returns 
print(y)
print(z)
#use of not
a = 10
b = 20
print(not(a<=b))
print(not(a >= b))#not returns opposite condition 