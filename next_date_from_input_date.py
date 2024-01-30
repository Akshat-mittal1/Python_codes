# input
date_I=int(input("Enter the date-->"))
month_I=input("Enter the month-->").lower()
year_I=int(input("Enter the year-->"))


#creating months list

mon1=['jan','feb','mar','apr','may','june','july','aug','sep','oct','nov','dec']
mon2=["january", "february","march", "april","may", "june","july","august", "september", "october", "november","december"]
mon3=['1','2','3','4','5','6','7','8','9','10','11','12']
d31=mon1[0:7:2]+mon1[7::2]+mon2[0:7:2]+mon2[7::2]+mon3[0:7:2]+mon3[7::2]
d32=mon1+mon2+mon3
d30=[i for i in d32 if i not in d31]
del d30[0::5]
d28=['feb','february','2']


# checking month exist 
if (month_I in mon1):
    monthindex=mon1.index(month_I)
    m=mon1
elif (month_I in mon2):
    monthindex=mon2.index(month_I)
    m=mon2
elif (month_I in mon3):
    monthindex=mon3.index(month_I)
    m=mon3
else:
    print("invalid month")
    exit()

# working on dates
if(month_I in d31):
    if(date_I <=30):
        date_O=date_I+1
    elif(date_I == 31):
        date_O=1
        monthindex+=1
    else:
        print("invalid date")
        exit()
elif(month_I in d30):
    if(date_I <=29):
        date_O=date_I+1
    elif(date_I == 30):
        date_O=1
        monthindex+=1
    else:
        print("invalid date")
        exit()
elif(month_I in d28):
    if((year_I%4==0 and year_I%100!=0) or year_I%400==0):
        if(date_I <=28):
            date_O=date_I+1
        elif(date_I == 29):
            date_O=1
            monthindex+=1
        else:
            print("invalid date")
            exit()
        
    else:
        if(date_I <=27):
            date_O=date_I+1
        elif(month_I == 28):
            date_O=1
            monthindex+=1
        else:
            print("invalid date")
            exit()

# year
if (monthindex==12):
    year_O=year_I+1
    monthindex=0
else:
    year_O=year_I

#final output
print('date--> ',date_O)
print('month-->',m[monthindex])
print("year-->",year_O)      

