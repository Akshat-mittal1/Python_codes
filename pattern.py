# Enter your code here. Read input from STDIN. Print output to STDOUTaZZ CCD

num1=int(input("enter the number-->"))
y=(num1//2)
z=y+1
num2=num1*3 
p=(num2-7)//2
for i in range(num1):
    z-=1
    for j in range(num1):
        if(i==y):
            continue

        elif(i!=y):
            if(j<z or j>=num1-z or j<(-z) or j>=num1+z ):
                print("---",end="")
            else:
                print(".|.",end="")
    
           
    for j in range(num2):
        if(i==y):
            if(j==p):
                print("WELCOME",end="")
            elif(j>p and j<p+7):
                continue
            else:
                print("-",end="")
    print("")                               
            
      
        
