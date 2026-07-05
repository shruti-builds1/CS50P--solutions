exp=input('Expression : ')
l=exp.split()
if l[1]=='+' :
    result=int(l[0]) + int(l[2])
    print(f'{result: .1f}')
elif l[1]=='-' :
    result=int(l[0]) - int(l[2])
    print(f'{result: .1f}')
elif l[1]=='*' :
    result=int(l[0]) * int(l[2])
    print(f'{result: .1f}')
elif l[1]=='/' :
    result=int(l[0]) / int(l[2])
    print(f'{result: .1f}')