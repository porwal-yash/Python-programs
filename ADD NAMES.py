f=open("vibha100.txt",'w')
ab='ch'
while ab=='ch' or ab=='hi':
    a=input("enter your name:")
    b=input("if u want add names write (y/n)")
    if b=='y':
        ab='hi'
    else:
        ab='bye'
    f.write(a)
    f.write('\n')
   
f.close()
