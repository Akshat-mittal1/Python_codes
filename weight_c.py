weight=float(input("enter the weight :"))
unit=input("enter the unit :")
if unit.lower()=='k':
    weight*=0.45
    print(weight, "lbs")
else :
    weight//=0.45
    print(weight,"kg")
