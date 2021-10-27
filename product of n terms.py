#product of n terms using recursion
def vinay(n):
    if n==1:
        return 1
    else:
        return (n+vinay(n-1))
no=int(input("enter a no"))
product=vinay(no)
print("the product of n terms is",product)
#product of n terms using loop
a=int(input("enter a no"))
t=1
for i in range(1,a+1):
    t=i*t
print("the product of n terms is",t)


