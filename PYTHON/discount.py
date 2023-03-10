while True:
    MP = int(input("enter marked price->"))
    discount_p = int(input("enter discount in percent->"))
    discount_r = discount_p/100 *MP 
    total_amount = MP - discount_r
    print(total_amount)



