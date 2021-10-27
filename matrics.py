g=input('enter order of 1st matrics')
if g=='2*2':
    c=int(input('enter a11'))
    d=int(input('enter a12'))
    e=int(input('enter a21'))
    f=int(input('enter a22'))
    k= 1
    for i in range(1,3):
        for j in range(1,3):
            if k/2==1:
                print(d,end='')
            elif k/3==1:
                print(e,end='')
            elif k/4==1:
                print(f,end='')
            else:
                print(c,end='')
            k=k+1
elif g=='1*1':
    x=int(input('enter a11'))
    print(x)
elif g=='3*3':
     aa=int(input('enter a11'))
     bb=int(input('enter a11'))
     cc=int(input('enter a11'))
     dd=int(input('enter a11'))
     ee=int(input('enter a11'))
     ff=int(input('enter a11'))
     gg=int(input('enter a11'))
     hh=int(input('enter a11'))
     ii=int(input('enter a11'))
     k=1
     for i in range(1,4):
         for j in range(1,4):
                if k/2==1:
                   print(bb,end='')
                elif k/3==1:
                   print(cc,end='')
                elif k/4==1:
                   print(dd,end='')
                elif k/5==1:
                   print(ee,end='')
                elif k/6==1:
                   print(ff,end='')
                elif k/7==1:
                   print(gg,end='')
                elif k/8==1:
                   print(hh,end='')
                elif k/9:
                   print(ii,end='')
                else:
                   print(aa,end='')
                k=k+1
else:
    print('invalid order')
g=input('enter order of 2nd matrics')
if g=='2*2':
    ccc=int(input('enter a11'))
    ddd=int(input('enter a12'))
    eee=int(input('enter a21'))
    fff=int(input('enter a22'))
    k= 1
    for i in range(1,3):
        for j in range(1,3):
            if k/2==1:
                print(ddd,end='')
            elif k/3==1:
                print(eee,end='')
            elif k/4==1:
                print(fff,end='')
            else:
                print(ccc,end='')
            k=k+1
elif g=='1*1':
    xx=int(input('enter a11'))
    print(xx)
elif g=='3*3':
     aaa=int(input('enter a11'))
     bbb=int(input('enter a11'))
     ccc=int(input('enter a11'))
     ddd=int(input('enter a11'))
     eee=int(input('enter a11'))
     fff=int(input('enter a11'))
     ggg=int(input('enter a11'))
     hhh=int(input('enter a11'))
     iii=int(input('enter a11'))
     k=1
     for i in range(1,4):
         for j in range(1,4):
                if k/2==1:
                    print(bbb,end='')
                elif k/3==1:
                    print(ccc,end='')
                elif k/4==1:
                    print(ddd,end='')
                elif k/5==1:
                    print(eee,end='')
                elif k/6==1:
                    print(fff,end='')
                elif k/7==1:
                    print(ggg,end='')
                elif k/8==1:
                    print(hhh,end='')
                elif k/9:
                    print(iii,end='')
                else:
                    print(aaa,end='')
                k=k+1
else:
    print('invalid order')
z=input('Do you want o add(0),subract(1)or do nothing(2)')
if z=='0' and g=='2*2':
    j=c+ccc
    k=d+ddd
    l=e+eee
    m=f+fff
    k=1
    for i in range(1,3):
        for j in range(1,3):
            if k/2==1:
                print(k,end='')
            elif k/3==1:
                print(l,end='')
            elif k/4==1:
                print(m,end='')
            else:
                print(j,end='')
            k=k+1
elif z=='0' and g=='1*1':
    n=x+xx
    print(n)
elif z=='0' and g=='3*3':
    o=aa+aaa
    p=bb+bbb
    q=cc+ccc
    r=dd+ddd
    s=ee+eee
    t=ff+fff
    u=gg+ggg
    v=hh+hhh
    w=ii+iii
    k=1
    for i in range(1,4):
        for j in range(1,4):
                if k/2==1:
                    print(p,end='')
                elif k/3==1:
                    print(q,end='')
                elif k/4==1:
                    print(r,end='')
                elif k/5==1:
                    print(s,end='')
                elif k/6==1:
                    print(t,end='')
                elif k/7==1:
                    print(u,end='')
                elif k/8==1:
                    print(v,end='')
                elif k/9:
                    print(w,end='')
                else:
                    print(o,end='')
                k=k+1
elif z=='1' and z=='1*1':
    xxx=x-xx
    print(xxx)
elif z=='1' and z=='2*2':
    j=c-ccc
    k=d-ddd
    l=e-eee
    m=f-fff
    k=1
    for i in range(1,3):
        for j in range(1,3):
            if k/2==1:
                print(k,end='')
            elif k/3==1:
                print(l,end='')
            elif k/4==1:
                print(m,end='')
            else:
                print(j,end='')
            k=k+1
elif z=='1' and z=='3*3':
    o=aa+aaa
    p=bb-bbb
    q=cc-ccc
    r=dd-ddd
    s=ee-eee
    t=ff-fff
    u=gg-ggg
    v=hh-hhh
    w=ii-iii
    k=1
    for i in range(1,4):
        for j in range(1,4):
            if k/2==1:
                print(p,end='')
            elif k/3==1:
                print(q,end='')
            elif k/4==1:
                print(r,end='')
            elif k/5==1:
                print(s,end='')
            elif k/6==1:
                print(t,end='')
            elif k/7==1:
                print(u,end='')
            elif k/8==1:
                print(v,end='')
            elif k/9:
                print(w,end='')
            else:
                print(o,end='')
                k=k+1
else:
    print('invalid no.')
    
    
    
    
    
    
    
