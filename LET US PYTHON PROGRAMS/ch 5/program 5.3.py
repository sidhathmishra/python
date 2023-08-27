percentage = int(input("enter exam percentage >>>"))
if percentage >= 60 :#checking percentage between 100 and 60
    print(" excellent! First division")

elif percentage >= 50:#checking percentage between 59 and 50
    print("good! Second division")

elif percentage >= 40:#checking percentage between 49 and 40
    print("can do better! Third division")

else:#checking percentage less than 40 
    print("better luck next time!","failed!")