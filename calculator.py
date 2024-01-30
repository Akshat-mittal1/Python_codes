num1=int(input("enter the first number-->"))
num2=int(input("enter the second number-->"))

   
print("we will be using *,-,+,/,%,**  -->")
print("press 1 for *")
print("press 2 for /")
print("press 3 for -")
print("press 4 for +")
print("press 5 for %")
print("press 6 for **")
print("press 7 for //")
print("press 8 for &")
print("press 9 for |")
print("press 10 for ~")
ch=int(input("enter your choice-->"))
if (ch==1):
    c=num1*num2
    print("the solution of the equation",num1 ,"*",num2,"is",c)
elif (ch==4):
    c=num1+num2
    print("the solution of the equation",num1,'+',num2,'is',c)
elif (ch==3):
    print(" press 1 for",num1,'-',num2 ,' or press 2 for ',num2,'-',num1)
    y=int(input("-->"))
    if (y==1):
        c=num1-num2
        print("the solution of the equation",num1,'-',num2,'is',c)
    
    elif (y==2):
        c=num2-num1
        print("the solution of the equation",num2,'-',num1,'is',c)
        
elif (ch==2):
    print(" press 1 for",num1,'/',num2 ,' or press 2 for ',num2,'/',num1)
    y=int(input("-->"))
    if (y==1):
        c=num1/num2
        print("the solution of the equation ",num1,'/',num2,'is',c)
        
    elif (y==2):
        c=num2/num1
        print("the solution of the equation",num2,'/',num1,'is',c)

elif (ch==5):
    print(" press 1 for",num1,'%',num2 ,' or press 2 for ',num2,'%',num1)
    y=int(input("-->"))
    if (y==1):
        c=num1%num2
        print("the solution of the equation ",num1,'%',num2,'is',c)
        
    elif (y==2):
        c=num2%num1
        print("the solution of the equation",num2,'%',num1,'is',c)
elif(ch==6):
   print(" press 1 for",num1,'**',num2 ,' or press 2 for ',num2,'**',num1)
   y=int(input("-->"))
   if (y==1):
       c=num1**num2
       print("the solution of the equation ",num1,'**',num2,'is',c)
   elif (y==2) :
       c=num2**num1
       print("the solution of the equation",num2,'**',num1,'is',c)
elif(ch==7):
   print(" press 1 for",num1,'//',num2 ,' or press 2 for ',num2,'//',num1)
   y=int(input("-->"))
   if (y==1):
       c=num1//num2
       print("the solution of the equation ",num1,'//',num2,'is',c)
   elif (y==2) :
       c=num2//num1
       print("the solution of the equation",num2,'//',num1,'is',c)
elif(ch==8):
    c=num1&num2
    print("the solution of the equation",num2,'&',num1,'is',c)
elif(ch==9):
    c=num1|num2
    print("the solution of the equation",num2,'|',num1,'is',c)
elif(ch==10):
    c=~(num1)
    print("the solution of the equation ~",num1,'is',c)

