user=input('Input: ')
l=[]
for k in user :
    if k.lower() not in 'aeiou' :
        l.append(k)
print('Output: \n')
for i in l :
    print(i,end='')
print()