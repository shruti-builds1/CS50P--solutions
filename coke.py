print('Amount Due: 50')
l=[]
due=50
while True :
    if due>0 :
        insert=int(input('Insert Coin: '))
        if insert in (10,5,25) :
            l.append(insert)
        else :
            l.append(0)
        due-=l[-1]
        if due>0 :
            print('Amount Due:',due)
        else :
            pass
    else :
        print('Charge Owed:',abs(due))
        break


            

