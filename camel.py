user=input('Camel Case : ')
l=[]
for i in user : 
    if i.islower()==True :
        l.append(i)
    else :
        string=i.lower()        
        l.extend(['_',string])
print('Snake Case : ',end='')
for k in l :
    print(k,end='')

print()