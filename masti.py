s=[]
ch='y'
while ch=='y' or ch=='Y':
    print('1 push')
    print('2 pop')
    print('3 nothing')
    a=int(input('enter what u want?'))
    if a==1:
        b=input('enter any value')
        s.append(b)
        print('your value is added')
    elif a==2:
        if s==[]:
            print("stack is empty")
        else:
            s.pop()
            print("value is deleted from stack")
    else:
        print("ok")
        print("your stack is")
        print(s)
        break
        
