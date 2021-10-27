#quaratic equation
a=int(input('enter a'))
b=int(input('enter b'))
c=int(input('enter c'))
d=b*b-(4*a*c)
if d==1 or d==4 or d==9 or d==16 or d==25 or d==36 or d==49 or d==64 or d==81 or d==100 or d==121 or d==144 or d==169 or d==196 or d==225 or d==256 or d==289 or d==324 or d==361 or d==400:
    if a==0:
        print('the value of a should not be zero')
    else:
        if d>0:
            e=(-b+d**0.5)/(2*a)
            f=(-b-d**0.5)/(2*a)
            print('roots are real and unequal')
            print('root 1 is',e)
            print('root 2 is',f)
        else:
            print('invalid')
else:
    if d==0:
        g=-b/(2*a)
        h=-b/(2*a)
        print('roots are real and equal')
        print('root 1 is',g)
        print('root 2 is',h)
    elif d<0:
        print('roots are complex and imaginary')
    else:
        print('diffcult to find')
        
