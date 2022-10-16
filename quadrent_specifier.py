x=int(input("Enter the x :"))
y=int(input("Enter the y :"))
if (x>0 and y>0):
    print('It is in first Quadernt')
elif (x<0 and  y>0):
    print('It is in second Quadernt')
elif (x<0 and y<0):
    print('It is in third Quadernt')   
elif (x>0 and y<0):
    print('It is in fourth Quadernt')    
elif (x==0 and y==0):
    print('It is origin')
elif x==0:
    print('It is on Y-axis')    
elif y==0:
    print('It is on X-axis')      

    
    
    
    
    