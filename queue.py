q=[]

def Enqueue(passenger):
    a=input("enter passenger name ")
    passenger.append(a)
    rear=len(passenger)-1
    return passenger

def Dequeue(passenger):
    if passenger==[]:
        return 'underflow'
    else:
        x=passenger.pop()
        print("Deleted Element: ",x)
    if len(passenger)==0:
        rear=front=None
    return passenger
while(True):
    print("Enter 1 for enqueue \nEnter 2 for dequeue \nEnter 3 for display \nEnter 4 for exit \n")
    n=int(input())
    if n==1:
        q=Enqueue(q)
    elif n==2:
        q=Dequeue(q)
    elif n==3:
        for i in q:
            print(i)
    elif n==4:
        print("Exiting")
        break
    else:
        print("Invalid Entry")
 
