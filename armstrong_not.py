num1=int(input("enter the number to check whether the number is armstrong or not :"))
a=num1
sum1=0
while(num1!=0):
    rem=num1%10
    sum1+=(rem**3)
    num1=num1//10
if(a==sum1):
    print("the given number is armstrong")
else:
    print("the given number is not armstrong")
