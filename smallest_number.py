print("Hello brother !")
print('lets find the smallest number from the given number')
enter2=eval(input('number of input to be enter-->'))
enter1=eval(input('enter your numbers -->'))
x=enter1
for i in range(enter2-1):
    enter1=eval(input('enter your numbers -->'))
    if enter1<x:
        x=enter1
print('smallest number amoung the given numbers is ',x)
