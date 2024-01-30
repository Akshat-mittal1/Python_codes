#car automation
print('command allowed:\nstart  stop  quit  help')

while 1:
    cmd=input("enter the command :")
    cmd=cmd.lower()
    if (cmd=='start'):
        print("car started")
    elif(cmd=='stop'):
        print('car stoped')
    elif(cmd=='help'):
        print("sending help")
    elif(cmd=="quit"):
        print("driver exit the car ")
    else:
        print("invalid choice")
        a=input('to continue the code press 1 :')
        if (a=='1'):
            continue
        else:
            break
    
