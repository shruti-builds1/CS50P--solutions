L=[]
line1=input('Enter a line : ')
L.append(line1)
while True :
    choice=input('Want to add more line(s)? [YES/NO] : ').upper()
    if choice=='NO' :
        break
    elif choice=='YES' :
        pass
    else:
        print('Invalid Answer, please try again!')
        continue
    line2=input('Enter a line : ')
    L.append(line2)
for k in L : 
    l=k.split()
    for i in range(0,len(l)-1,1) :
        print(l[i],end='...')
    print(l[-1])

# l=line.split()
# for k in range(0,len(l)-1,1)  :
#     print(l[k],end='...')
# print(l[-1])