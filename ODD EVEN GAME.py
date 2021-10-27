import random
user=input("enter your name")
print('now u would be treated as',user)
#storing game data
f=open("databaseofgame.txt",'a')
a=input('what do you want to choose odd or even')
b=int(input('enter a no'))
c=random.randrange(1,7)
print('computer number is',c)
rr=0
rrr=0
rrrr=0
rrrrr=0
q=0
d=b+c
if d%2==0:
    r='even'
else:
    r='odd'
if a==r:
    print(user,' won the toss')
    w=int(input('what you want to choose batting(1) or bowling(2)'))
    if w==1:#batting of user
        print(user,'choose to bat')
        yy='ch'
        rr=0
        while yy=='not out' or yy=='ch':
            aa=int(input('enter your number batting from 0 - 6'))
            bb=random.randrange(1,7)
            if aa==bb:
                print('sorry',user,' you  are out')
                yy=1
            else:
                print(user,'your score is')
                print(aa,'runs')
                yy='not out'
                rr+=aa
                print('computer no is ',bb)
            print(user,'your total score is',rr)
            q=rr
        print('computer need',q+1,'runs to win the match') # runs to win
    elif w==2:#bowling of user
        print(user,'you choose to bowl')
        yyy='ch'
        rrr=0
        while yyy=='not out' or yyy=='ch':
            aaa=int(input('enter your bowling number from 0 - 6'))
            bbb=random.randrange(1,6)
            if aaa==bbb:
                xxx='computer is out'
                print(xxx)
                yyy=1
            else:
                print('computer score is')
                print(bbb,'runs')
                yyy='not out'
                rrr+=bbb
            print('computer total score is',rrr)
            q=rrr
        print(user,'you need',q+1,'runs to win the match') #runs to win
    else:
        print('invalid number you choose')
else:
    print(user,'you loose')
    z=random.randrange(0,2)
    if z==0:#batting of computer
        print('computer choose to bat')
        yyyy='ch'
        rrrr=0
        while yyyy=='not out' or yyyy=='ch':
            aaaa=int(input('enter your bowling number from 0 - 6'))
            bbbb=random.randrange(1,6)
            if aaaa==bbbb:
                xxxx='computer is out'
                print(xxxx)
                yyyy=1
            else:
                print('computer score is')
                print(bbbb,'runs')
                yyyy='not out'
                rrrr+=bbbb
            print('computer total score is',rrrr)
            q=rrrr
        print(user,'you need',q+1,'runs to win the match') #runs to win
    elif z==1:#bowling of computer
        print('computer choose to bowl')
        yyyyy='ch'
        rrrrr=0
        while yyyyy=='not out' or yyyyy=='ch':
            aaaaa=int(input('enter your number batting from 0 - 6'))
            bbbbb=random.randrange(1,6)
            if aaaaa==bbbbb:
                print(user,'sorry you are out')
                yyyyy=1
            else:
                print(user,'your score is')
                print(aaaaa,'runs')
                yyyyy='not out'
                rrrrr+=aaaaa
                print('computer no is ',bbbbb)
            print(user,'your total score is',q)
            q=rrrrr
        print('computer need',q+1,'runs to win the match') #runs to win
    else:
        print('game id terminating') 
if q==rr: #2nd turn of bowling of user  1
    print('Now,bolwing of',user)
    cccc='vi'
    vvvv=0
    l=0
    while cccc=='not out' or cccc=='vi':
        nnnn=int(input('enter your bowling number from 0 - 6'))
        mmmm=random.randrange(1,6)
        if nnnn==mmmm:
            oooo='computer is out'
            print(oooo)
            cccc=1
            if l<q:
                vi='  win'
                print(user,'you won the match')
                break
            elif l==q:
                vi='  draw'
                print('match was draw')
                break
        else:
            print('computer score is')
            print(mmmm,'runs')
            cccc='not out'
            vvvv+=mmmm
        l=vvvv
        print('computer total score is',l)
        if l>q:
            vi='  loose'
            print('  computer won')
            break
elif q==rrr:#2nd turn of batting of user   2
    print('Now,batting of',user)
    ccccc='vi'
    vvvvv=0
    l=0
    while ccccc=='not out' or ccccc=='vi':
        nnnnn=int(input('enter your number batting from 0 - 6'))
        mmmmm=random.randrange(1,6)
        if nnnnn==mmmmm:
            print(user,'sorry you are out')
            ccccc=1
            if l<q:
                vi='  loose'
                print('computer won the match')
                break
            elif l==q:
                vi='  draw'
                print('match was draw')
                break
        else:
            print(user,'your score is')
            print(nnnnn,'runs')
            yy='not out'
            vvvvv+=nnnnn
            print('computer no is ',mmmmm)
        l=vvvvv
        print(user,'your total score is',l)
        if l>q:
            vi=' win'
            print(user,' won')
            break
elif q==rrrr:# 2nd turn of bowling of computer   3
    print('Now bolwing of computer')
    cc='vi'
    vv=0
    l=0
    while cc=='not out' or cc=='vi':
        nn=int(input('enter your number batting from 0 - 6'))
        mm=random.randrange(1,6)
        if nn==mm:
            print(user,'sorry you are out')
            cc=1
            if l<q:
                vi='  loose'
                print('computer won the match')
                break
            elif l==q:
                vi='  draw'
                print('match was draw')
                break
        else:
            print(user,'your score is')
            print(nn,'runs')
            cc='not out'
            vv+=nn
            print('computer no is ',mm)
        l=vv
        print(user,'your total score is',l)
        if l>q:
            vi='  win'
            print(user,' won')
            break
elif q==rrrrr:#2nd turn of batting of computer   4 
    print('Now,batting of computer')
    ccc='vi'
    vvv=0
    l=0
    while ccc=='not out' or ccc=='vi':
        nnn=int(input('enter your bowling number from 0 - 6'))
        mmm=random.randrange(1,6)
        if nnn==mmm:
            ooo='computer is out'
            print(ooo)
            ccc=1
            if l<q:
                vi='  win'
                print(user,' won the match')
                break
            elif l==q:
                vi='  draw'
                print('match was draw')
                br
        else:
            print('computer score is')
            print(mmm,'runs')
            ccc='not out'
            vvv+=mmm
        l=vvv
        print('computer total score is',l)
        if l>q:
            vi='  loose'
            print('computer won')
            break
else:
    print('programm get crashed')
f.write(user)
f.write(vi)
f.write('\n')
f.close()
print("Game Terminates Successfully")
print("your preformance has been saved successfully")

    
        
    
    
    
          
