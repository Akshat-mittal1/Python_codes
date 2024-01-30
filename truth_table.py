print("Truth table :")
print("A\tB\tA&B\tA|B\tA^B")
for A in range (2):
    for B in range(2):
        a=A&B
        b=A|B
        c=A^B
        print(A,"\t",B,"\t",a,"\t",b,"\t",c)
        
