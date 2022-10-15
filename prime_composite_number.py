n=int(input("Enter the Number :"))
com=0
for i in range(2, n) :
    if(n%i==0):
        com=1
        print("Least divider is : ", i)
        break
if(com==1):
    print(str(n)+" is a Composite Number ")
else :
    print(str(n)+" is a Prime Number ")    
         
       
        
     


