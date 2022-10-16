x=int(input('Enter the number :'))
rev=0
flag=0
while x>0:
    r=x%10
    if r==0:
        flag=1
    rev=rev*10+r
    x=x//10
if bool(flag):
    print(0, end="")
print(rev)