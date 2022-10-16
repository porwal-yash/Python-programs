x=int(input('Enter an Integer Value :'))
y=int(input('\n\n Enter the other greater Integer :'))
for num in range(x,y+1):
    if num>1:
           for i in range(2,num):
               if(num%i)==0:
                    break
           else:
                print (num)
             