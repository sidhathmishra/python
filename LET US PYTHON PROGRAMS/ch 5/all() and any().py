a ,b , c = 10 , 20 , 30

condition = all((a>5,b>5,c<= 10))# false, as last condition is false
print(condition)
condition2 = any((a <=8, b<6,c == 30))#true, as last condition  is true
print(condition2)    

