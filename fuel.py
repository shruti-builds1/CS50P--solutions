# def main() :
#     x=get_percentage('Fraction: ')
#     print(x)

# def get_percentage(prompt) :
#     while True :
#         try :
#             l=input(prompt).strip().split('/')
#             if int(l[0])<=int(l[1]) and int(l[0])>=0 :       # to check numerator<denominator and both are positive
#                 y=(int(l[0])/int(l[1]))*100
#                 z=round(y)                                   # round off to nearest int
#                 if z<=1 :
#                     return 'E'
#                 elif z>=99 :
#                     return 'F'
#                 else :
#                     return str(z)+'%'
#             else :
#                 pass
            
#         except ValueError :                       # error check
#             pass
#         except ZeroDivisionError :
#             pass 

# main()

def main():
    while True :
        user=input('Fraction: ')
        ans=convert(user)
        if type(ans)==int :
            break

    # user=input('Fraction: ')
    print(gauge(ans))



def convert(fraction):
    # try :
            l=fraction.strip().split('/')
            if int(l[1])==0 :
                k=(int(l[0])/int(l[1]))*100
            # elif l[0].startswith('-') :
            #     #  j=int('cat')/int('dog')
            #     j=(int(l[0][0])/int(l[1]))*100
            # elif l[1].startswith('-') :
            #      p=(int(l[0])/int(l[1][0]))*100

            elif int(l[0])>int(l[1]) :
                 i=int(fraction)
            elif int(l[0])<=int(l[1])  :
                y=(int(l[0])/int(l[1]))*100
                if str(round(y)).startswith('-') :
                     j=int(fraction)
                else :
                    return round(y)
            # else :
            #     return f'Invalid fraction'

    # except ValueError :
    #     return f'Invalid fraction'

    # except ZeroDivisionError :
    #     return f'Can not divide by zero'


def gauge(percentage):
    if percentage<=1 :
        return f'E'
    elif percentage>=99 :
        return f'F'
    else :
        return f'{str(percentage)}%'

if __name__ == "__main__":
    main()

            




    
