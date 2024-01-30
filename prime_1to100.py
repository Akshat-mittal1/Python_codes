#prime list 1-100

for i in range(2,101):
    a=i
    for j in range(2,i):
        if(i%j==0):
            a-=1
            break
        else:
            continue
    if(i==a):
        print(i,end='  ')
    

