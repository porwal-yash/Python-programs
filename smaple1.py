#vinay
import random
a=input('are you ready player1 yes or no')
b=input('Are you ready player2 yes or no')
c=int(input("enter your no"))
d=int(input("enter your no"))
print('player 1 no =',c)
print('player 2 no =',d)
rr=0
rrr=0
rrrr=0
rrrrr=0
q=0
d=c+d
if d%2==0:
    r='even'
else:
    r='odd'
if a==r:
    print('player1 won the toss')
    w=int(input('what player1  want to choose batting(1) or bowling(2)'))
    if w==1:#batting of player1
        print('palyer1 choose to bat')
        yy='ch'
        rr=0
        while yy=='not out' or yy=='ch':
            aa=int(input('enter your number batting from 0 - 6'))
            bb=int(input('enter your number bolwling from 0-6'))
            if aa==bb:
                xx='sorry palyer1 is out'
                print(xx)
                yy=1
            else:
                print('palyer1 score is')
                print(aa,'runs')
                yy='not out'
                rr+=aa
            print('player1 total score is',rr)
            q=rr
        print('player2 needs',q+1,'runs to win the match') # runs to win
    elif w==2:#bowling of player1`
        print('player1 choose to bowl')
        yyy='ch'
        rrr=0
        while yyy=='not out' or yyy=='ch':
            bbb=int(input('enter palyer2 batting number from 0 - 6'))
            aaa=int(input('enter player1 bowling number from 0 - 6'))
            if aaa==bbb:
                xxx='player2 is out'
                print(xxx)
                yyy=1
            else:
                print('player2 score is')
                print(bbb,'runs')
                yyy='not out'
                rrr+=bbb
            print('player total score is',rrr)
            q=rrr
        print('player1 need',q+1,'runs to win the match')
    else:
        print('invalid number you choose')
else:
    print('player2 won the toss')
    z=int(input('what player2  want to choose batting(0) or bowling(1)'))
    if z==0:#batting of player2
        print('palyer2 choose to bat')
        yyyy='ch'
        rrrr=0
        while yyyy=='not out' or yyyy=='ch':
            bbbb=int(input('enter palyer2 batting number from 0 - 6'))
            aaaa=int(input('enter player1 bowling number from 0 - 6'))
            if aaaa==bbbb:
                xxxx='player2 is out'
                print(xxxx)
                yyyy=1
            else:
                print('computer score is')
                print(bbbb,'runs')
                yyyy='not out'
                rrrr+=bbbb
            print('player2 total score is',rrrr)
            q=rrrr
        print('palyer1 needs',q+1,'runs to win the match')
    elif z==1:#bowling of player2
        print('palyer2 choose to bowl')
        yyyyy='ch'
        rrrrr=0
        while yyyyy=='not out' or yyyyy=='ch':
            aaaaa=int(input('enter palyer1 number batting from 0 - 6'))
            bbbbb=int(input('enter player2 number bowling from 0 - 6'))
            if aaaaa==bbbbb:
                xxxxx='sorry player1 are out'
                print(xxxxx)
                yyyyy=1
            else:
                print('player1 score is')
                print(aaaaa,'runs')
                yyyyy='not out'
                rrrrr+=aaaaa
            print('palyer1 total score is',q)
            q=rrrrr
        print('player2 needs',q+1,'runs to win the match') 
    else:
        print('game is terminating')
        print('terminated,PLEASE RESTARET THE GAME')
if q==rr: #2nd turn of bowling of player1
    print('Now,bolwing of player1')
    cccc='vi'
    vvvv=0
    l=0
    while cccc=='not out' or cccc=='vi':
        mmmm=int(input('enter player2 batting number from 0 - 6'))
        nnnn=int(input('enter palyer1 bowling number from 0 - 6'))
        if nnnn==mmmm:
            oooo='player2 is out'
            print(oooo)
            cccc=1
            if l<q:
                print('player1 won the match')
                break
            elif l==q:
                print('match was draw')
                break
        else:
            print('player2 score is')
            print(mmmm,'runs')
            cccc='not out'
            vvvv+=mmmm
        l=vvvv
        print('player2 total score is',l)
        if l>q:
            print('player2 won')
            break
elif q==rrr:#2nd turn of batting of player1
    print('Now,batting of player1')
    ccccc='vi'
    vvvvv=0
    l=0
    while ccccc=='not out' or ccccc=='vi':
        nnnnn=int(input('enter player1 number batting from 0 - 6'))
        mmmmm=int(input('enter palyer2 number bowling from 0 - 6'))
        if nnnnn==mmmmm:
            ooooo='sorry player1 is out'
            print(ooooo)
            ccccc=1
            if l<q:
                print('player2 won the match')
                break
            elif l==q:
                print('match was draw')
                break
        else:
            print('palyer1 score is')
            print(nnnnn,'runs')
            yy='not out'
            vvvvv+=nnnnn
        l=vvvvv
        print('player1 total score is',l)
        if l>q:
            print('palyer1 won')
            break
elif q==rrrr:# 2nd turn of bowling of player2
    print('Now bolwing of palyer2')
    cc='vi'
    vv=0
    l=0
    while cc=='not out' or cc=='vi':
        nn=int(input('enter player1 number batting from 0 - 6'))
        mm=int(input('enter player2 number bowling from 0 - 6'))
        if nn==mm:
            oo='sorry player1 are out'
            print(oo)
            cc=1
            if l<q:
                print('palyer2 won the match')
                break
            elif l==q:
                print('match was draw')
                break
        else:
            print('player1 score is')
            print(nn,'runs')
            cc='not out'
            vv+=nn
        l=vv
        print('palyer1 total score is',l)
        if l>q:
            print('player1 won')
            break
elif q==rrrrr:#2nd turn of batting of palyer2
    print('Now,batting of player2')
    ccc='vi'
    vvv=0
    l=0
    while ccc=='not out' or ccc=='vi':
        nnn=int(input('enter player1 bowling number from 0 - 6'))
        mmm=int(input('enter player2 batting number from 0 - 6'))
        if nnn==mmm:
            ooo='computer is out'
            print(ooo)
            ccc=1
            if l<q:
                print('palyer1 won the match')
                break
            elif l==q:
                print('match was draw')
                br
        else:
            print('player2 score is')
            print(mmm,'runs')
            ccc='not out'
            vvv+=mmm
        l=vvv
        print('player2 total score is',l)
        if l>q:
            print('palyer2 won')
            break
else:
    print('programm get crashed')

    
        
    
    
    
          
