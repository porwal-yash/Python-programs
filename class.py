def push(stack):
    bno=int(input("enter book no."))
    bname=input("enter name")
    bprice=float(input("enter"))
    bitem=(bno,bname,bprice)
    stack.append(bitem)
    
stack=[]
push(stack)
print(stack)
