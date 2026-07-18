
l=[]
while True :
    try :
        user=input('Name: ')
        l.append(user)

    except EOFError :
        print()
        print('Adieu, adieu, to',l[0],end='')
        comma=len(l)-2
        if comma>0 :
            print(',',end=' ')
            for k in range(1,comma+1) :
                print(l[k],end=', ')
            print('and',l[-1])

        elif comma==0 :
            print(' and',l[1])

        else:
            print('\n')

        break
# since \n by any means was not there it didn't go in the fresh new line



