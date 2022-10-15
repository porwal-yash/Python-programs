x=int(input('Enter an Integer Value : '))
if x%2==0:
    print(x, 'is an even number')
else :
    print(x, 'is an odd number')
y=int(input('\n\nEnter an Integer Value :'))
if  y>1:
    for i in range(2,y):
        if (y%i)==0:
            print('\t',y,'is not a prime number')
            break
    else:
        print('\t',y,'is a prime number')
else:
    print('invalid number')

