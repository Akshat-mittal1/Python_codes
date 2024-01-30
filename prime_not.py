#prime or not

num1=int(input("enter the number to check whether the number is prime or not :"))
for i in range(num1):
    if(i<=1):
        continue
    elif(num1%i==0):
        print("the given number is not prime")
        break
    else:
        continue
if(i+1==num1):
    print("the given number is prime")
        
