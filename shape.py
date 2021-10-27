a=input('enter a shape name')
if a=='circle' or a=='Circle':
    b=int(input('enter radius of the circle'))
    c=input('enter what you want to find area(1) or circumference(2)')
    if c=='1':
            print('area of circle is',3.14*b*b)
    elif c=='2':
            print('circumference of circle is',2*3.14*b)
    else:
            print('invalid number')
elif a=='rectangle' or a=='Rectangle':
            d=int(input('enter length of reactangle'))
            e=int(input('enter breadth of rectangle'))
            f=input('enter what you want to find area(1) or perimeter(2)')
            if f=='1':
                    print('area of rectangle is',d*e)
            elif f=='2':
                    print('perimeter of rectangle is',2*(d+e))
            else:
                 print('invalid no.')
else:
     print('invalid shape')
                    
                    
        
