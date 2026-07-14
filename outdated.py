D=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True :
    try :
        date=input('Date: ').strip()
        if '/' in date :
            l=date.split('/')
            if 1<=int(l[0])<=12 and 1<=int(l[1])<=31 :
                for k in range(len(l)-1) :
                    if 1<=int(l[k])<=9 :
                        l[k]='0'+l[k]
                    else :
                        pass
                print(l[2],l[0],l[1],sep='-')
                break

            else:
                pass
        elif ',' in date :
            t=date.split()
            if t[0] in D and 1<=int(t[1].rstrip(','))<=31 :
                t[0]=str(D.index(t[0])+1)
                t[1]=t[1].rstrip(',')
                for i in range(len(t)-1) :
                    if 1<=int(t[i])<=9 :
                        t[i]='0'+ t[i]
                    else :
                        pass
                print(t[2],t[0],t[1],sep='-')
                break
            else :
                pass

        else :
            pass
    except ValueError :
        pass





