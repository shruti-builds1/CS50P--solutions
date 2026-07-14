
D={}
while True :
    try :
        item=input('').upper()
        if item in D.keys() :
            D[item]+=1
        else :
            D[item]=1

    except EOFError :
        break
L=[]
for k in D :
    L.append(k)
L.sort()
for i in L :
    print(D[i],i)




