q=[]

def InsQueue(passenger):
    a=input("enter passenger name")
    passenger.append(a)
    rear=len(passenger)-1
    return passenger


def DelQueue(passenger):
    if passenger==[]:
        return 'underflow'
    else:
        passenger.pop(0)
    if len(passenger)==0:
        rear=front=None
    return passenger
 
