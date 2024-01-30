num1=int(input("enter the number to check whether the number is palidrome or not :"))
a=num1
sum1=0
while(num1!=0):
    rem=num1%10
    sum1=sum1*10+rem
    num1=num1//10
if(a==sum1):
    print("the given number is palidrome")
else:
    print("the given number is not palidrome")
