l=[]
line=input('Enter your lines(s) : ')
l.append(line)  
while True :
    # line=input('Enter your lines(s) : ')
    # l.append(line)
    choice=input('Want to add more lines? [YES/NO] : ').upper()

    if choice=='NO' :
        break
    elif choice=='YES':
        pass
    else :
        print('Invalid Answer, please try again!')
        # choice=input('Want to add more lines? [YES/NO] : ').upper()
        continue
    line=input('Enter your lines(s) : ')
    l.append(line)
for k in l : 
    print(k.lower())          
