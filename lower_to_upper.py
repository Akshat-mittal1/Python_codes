str1=input("enter the string :")
for i in str1:
    if(i.islower()):
        print(i.upper(),end="")
    else:
        print(i,end='')
