num1=int(input("enter the number to add the digits:"))
a=num1
sum1=0
while(num1!=0):
    rem=num1%10
    sum1=sum1+rem
    num1=num1//10
print("the sum of all the digits of ",a ,"is ",sum1)
