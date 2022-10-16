def DutchNationalFlag( a,n):
       mid=0
       low=0
       high=n-1
       while(mid<=high):
         if(a[mid]==0):
               temp= a[mid]
               a[mid]= a[low]
               a[low]= temp
               low+=1
               mid+=1
         elif  (a[mid]== 1):
                 mid+=1
         else:
               temp= a[mid]
               a[mid]= a[high]
               a[high]= temp
               high-=1
             

   
a=[0,1,0,1,2,2,2,0,0,1,0,0,0,0]
DutchNationalFlag(a,len(a))
print(a)
  
