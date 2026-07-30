import sys

if len(sys.argv)<2 :
    sys.exit('Too few command-line arguments')

elif len(sys.argv)>2 :
    sys.exit('Too many command-line arguments')

else :
    if sys.argv[1].endswith('.py') :
        try:
            with open(sys.argv[1]) as f :
                data=f.readlines()
                found=0
                for k in data:
                    if k.isspace():
                        continue
                    elif k.lstrip().startswith('#') :
                        continue
                    else :
                        found+=1
                print(found)

        except FileNotFoundError :
            sys.exit('File does not exist')
    else :
        sys.exit('Not a python file')
        