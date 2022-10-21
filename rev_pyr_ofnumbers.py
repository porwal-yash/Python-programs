def pattern(n):
    for i in range(1,n+1):
        for j in range(i,0,-1):
            print((str(j)+" "),end="")
        print()
n=int(input("Enter no. of rows: "))
pattern(n)