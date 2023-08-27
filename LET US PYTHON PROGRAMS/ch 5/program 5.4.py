marrige_status = input("enter marrige status >>>")
gender = input("enter gender >>>")
age = int(input("enter age >>>"))
if (marrige_status == "m") or (marrige_status == "u"and gender == "m" and age > 30)\
    or (marrige_status == "u"and gender == "f" and age > 25):
    print("insured")
else:
    print("not insured")