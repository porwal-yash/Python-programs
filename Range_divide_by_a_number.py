l=int(input('Enter lower :'))
u=int(input('Enter upper :'))
n=int(input('Enter the number to be devided by :'))
for i in range(l,u+1):  
    if (i%n==0):
        print(i)