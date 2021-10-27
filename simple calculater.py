a=int(input('enter a no'))
c=input('enter a operator')
b=int(input('enter a no'))
if c=='+':
    x=a+b
    print(x)
elif c=='-':
    x=a-b
    print(x)
elif c=='*':
    x=a*b
    print(x)
elif c=='/':
    x=a/b
    print(x)
else:
    print('invalid operator')
ch=input('want to add mores values (y/n)')
while ch=='y':
       d=input('enter a operator')
       e=int(input('enter no.'))
       if d=='+':
           s=x+e
           print(s)
           x=s
       elif d=='-':
           f=x-e
           print(f)
           x=f
       elif d=='*':
           j=x*e
           print(j)
           x=j
       elif d=='/':
           k=x/e
           print(k)
           x=k
       else:
           print('invalid operator')
       ch=input('want to do value(y/n)')

