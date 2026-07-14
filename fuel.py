def main() :
    x=get_percentage('Fraction: ')
    print(x)

def get_percentage(prompt) :
    while True :
        try :
            l=input(prompt).strip().split('/')
            if int(l[0])<=int(l[1]) and int(l[0])>=0 :       # to check numerator<denominator and both are positive
                y=(int(l[0])/int(l[1]))*100
                z=round(y)                                   # round off to nearest int
                if z<=1 :
                    return 'E'
                elif z>=99 :
                    return 'F'
                else :
                    return str(z)+'%'
            else :
                pass
            
        except ValueError :                       # error check
            pass
        except ZeroDivisionError :
            pass 

main()
            




    