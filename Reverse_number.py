x=int(input('Enter the number :'))
rev=0
while x>0:
    dig=x%10
    rev=rev*10+dig
    x=x//10
print(rev)




