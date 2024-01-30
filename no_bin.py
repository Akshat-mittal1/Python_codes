num1=int(input("enter the number-->"))
sum1=0
temp1=1
num2=num1
while (num2>=temp1):
    temp1*=2

while (temp1!=1):
        temp1/=2
        if (num2>=temp1):
            num2-=temp1
            sum1=(sum1*10)+1
        else:
            sum1=sum1*10
            
print("the conversion of ",num1,'in binary is ',sum1)
    
