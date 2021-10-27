#assinging subjects to random values
import random as rd
subjects=["Physics","Chemistry","Cs","English","Maths","Games"]

x21=subjects[0]
def no():
    x31=rd.choice(subjects)
    return x31
x31=no()
x41=rd.choice(subjects)
x51=rd.choice(subjects)
x61=rd.choice(subjects)
x71=rd.choice(subjects)
x81=rd.choice(subjects)
x91=rd.choice(subjects)
x22=subjects[0]
x32=rd.choice(subjects)
x42=rd.choice(subjects)
x52=rd.choice(subjects)
x62=rd.choice(subjects)
x72=rd.choice(subjects)
x82=rd.choice(subjects)
x92=rd.choice(subjects)
x23=subjects[0]
x33=rd.choice(subjects)
x43=rd.choice(subjects)
x53=rd.choice(subjects)
x63=rd.choice(subjects)
x73=rd.choice(subjects)
x83=rd.choice(subjects)
x93=rd.choice(subjects)
x24=subjects[0]
x34=rd.choice(subjects)
x44=rd.choice(subjects)
x54=rd.choice(subjects)
x64=rd.choice(subjects)
x74=rd.choice(subjects)
x84=rd.choice(subjects)
x94=rd.choice(subjects)
x25=subjects[0]
x35=rd.choice(subjects)
x45=rd.choice(subjects)
x55=rd.choice(subjects)
x65=rd.choice(subjects)
x75=rd.choice(subjects)
x85=rd.choice(subjects)
x95=rd.choice(subjects)
x26=subjects[0]
x36=rd.choice(subjects)
x46=rd.choice(subjects)
x56=rd.choice(subjects)
x66=rd.choice(subjects)
x76=rd.choice(subjects)
x86=rd.choice(subjects)
x96=rd.choice(subjects) 
#creating time table 
def table():
    column1="Day"
    column2="1"
    column3="2"
    column4="3"
    column5="4"
    column6="5"
    column7="6"
    column8="7"
    column9="8"
       
    row11="Monday"
    row21=x21
    row31=x31
    row41=x41
    row51=x51
    row61=x61
    row71=x71
    row81=x81
    row91=x91

    row12="Tuesday"
    row22=x22
    row32=x32
    row42=x42
    row52=x52
    row62=x62
    row72=x72
    row82=x82
    row92=x92

    row13="Wednesday"
    row23=x23
    row33=x33
    row43=x43
    row53=x53
    row63=x63
    row73=x73
    row83=x83
    row93=x93

    row14="Thrusday"
    row24=x24
    row34=x34
    row44=x44
    row54=x54
    row64=x64
    row74=x74
    row84=x84
    row94=x94

    row15="Friday"
    row25=x25
    row35=x35
    row45=x45
    row55=x55
    row65=x65
    row75=x75
    row85=x85
    row95=x95

    row16="Saturday"
    row26=x26
    row36=x36
    row46=x46
    row56=x56
    row66=x66
    row76=x76
    row86=x86
    row96=x96

    
    #condition for our time table

    randomsubjects=[row11,row31,row41,row51,row61,row71,row81,row91,row12,row32,row42,row52,row62,row72,row82,row92,row13,row33,row43,row53,row63,row73,row83,row93,row14,row34,row44,row54,row64,row74,row84,row94,row15,row35,row45,row55,row65,row75,row85,row95,row16,row36,row46,row56,row66,row76,row86,row96]
    g=0
    for i in randomsubjects:
        if i=="Games":
            g=g+1
    print("Games",g)

    m=0
    for i in randomsubjects:
        if i=="Maths":
            m=m+1
    print("Maths",m)

    e=0
    for i in randomsubjects:
        if i=="English":
            e=e+1
    print("English",e)

    cs=0
    for i in randomsubjects:
        if i=="Cs":
            cs=cs+1
    print("Cs",cs)

    c=0
    for i in randomsubjects:
        if i=="Chemistry":
            c=c+1
    print("Chemistry",c)

    p=0
    for i in randomsubjects:
        if i=="Physics":
            p=p+1
    print("Physics",p)

    # condition of no. peroids of a particular subject
    def yes():
        if g==1:
            if m==6:
                if e==6:
                    if cs==6:
                        if c==6:
                            if p==6:
                                print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(column1,column2,column3,column4,column5,column6,column7,column8,column9))
                                print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row11,row21,row31,row41,row51,row61,row71,row81,row91))
                                print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row12,row22,row32,row42,row52,row62,row72,row82,row92))
                                print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row13,row23,row33,row43,row53,row63,row73,row83,row93))
                                print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row14,row24,row34,row44,row54,row64,row74,row84,row94))
                                print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row15,row25,row35,row45,row55,row65,row75,row85,row95))
                                print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row16,row26,row36,row46,row56,row66,row76,row86,row96))
                            else:
                                print("no by physics")
                        else:
                            print("no by chemistry")
                    else:
                        print("no by cs")
                else:
                    print("no by english")
            else:
                print("no by maths")
        else:
            print("no by games")
            x31=no()
            vinay=yes()
            print(vinay)
            
    yes()
    
    



    print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(column1,column2,column3,column4,column5,column6,column7,column8,column9))
    print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row11,row21,row31,row41,row51,row61,row71,row81,row91))
    print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row12,row22,row32,row42,row52,row62,row72,row82,row92))
    print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row13,row23,row33,row43,row53,row63,row73,row83,row93))
    print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row14,row24,row34,row44,row54,row64,row74,row84,row94))
    print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row15,row25,row35,row45,row55,row65,row75,row85,row95))
    print("%-15s %-15s %-15s %-15s %-15s %-15s %-15s %-15s %s" %(row16,row26,row36,row46,row56,row66,row76,row86,row96))
   

















