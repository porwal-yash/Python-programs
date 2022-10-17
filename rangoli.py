n=int(input("Enter a number: "))
for i in range(n):
    a=""
    for r in range(i+1):
        a+=(chr(96+n-r))+"-"
    for x in range (i-1,-1,-1):
        a+=chr(96+n-x)+"-"
    print(a[:-1].center(4*n-3, "-"))
for i in reversed(range(n-1)):
    a=""
    for r in range(i+1):
        a+=(chr(96+n-r))+"-"
    for x in range (i-1,-1,-1):
        a+=chr(96+n-x)+"-"
    print(a[:-1].center(4*n-3, "-"))