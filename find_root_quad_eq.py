import math

print("enter the value of a,b and c to find the roots of the quadratic [a(x^2)+bx+c==0 ]equation-->")
a=int(input("enter the value of a :"))
b=int(input ("enter the value of b :"))
c=int(input("enter the value of c :"))
x=(b**2)-4*a*c
if (x<0):
    print("imaginary roots")
else:
    y=(-b+math.sqrt(x))/2*a;
    z=(-b-math.sqrt(x))/2*a;
    print("the roots of the quadratic equation are:",y,z)
