def stone():
    print('''press 1 for stone
press 2 for paper
press 3 for scissor''')
    import random
    count1=0
    count2=0
    comp=['stone','paper','scissor']
    while True:
        enter1=int(input("-->"))
        comp1=random.randint(1,3)
        if enter1==comp1:
            count2=count2+1
        elif enter1==1 and comp1==2:
            break
        elif enter1==1 and comp1==3:
            count1=count1+1
        elif enter1==2 and comp1==1:
            count1=count1+1
        elif enter1==2 and comp1==3:
            break
        elif enter1==3 and comp1==2:
            count1=count1+1
        elif enter1==3 and comp1==1:
            break
        else:
            print("invalid syntax")
    print("you got ",count1,"points congratulation")
    print("total number of draw ",count2)
stone()


playagain=eval(input("press '1 'as string to play again"))
if playagain==1:
    stone()
else:
    b=1
