quantity = int(input("enter quantity of items -->"))
price = float(input("enter price-->"))
if quantity > 1000:
    discount = 10

else :
    discount = 0

total_expense = quantity * price - quantity * price * discount/100
print("Total expense = ₹"+ str(total_expense))