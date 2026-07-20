import random

def main():
    ask=get_level()
    correct=0
    for k in range(10) :
        int1=generate_integer(ask)
        int2=generate_integer(ask)
        form=str(int1)+' + '+str(int2)+' = '
        try :
            ques1=int(input(form))
            ans=int1+int2
            if ques1==ans :
                correct+=1
                continue
            else :
                incorrect=0
                print('EEE')
                for i in range(2) :
                    try :
                        ques2=int(input(form))
                        if ques2==ans :
                            break
                        else :
                            incorrect+=1
                            print('EEE')
                            continue
                    except ValueError :
                         pass
                if incorrect==2 :
                    print(form,end='')
                    print(ans)
        except ValueError : 
            pass
    
    print('Score:',correct)

def get_level():
    try :
        # print('fuck')
        return int(input('Level: '))
    except ValueError :
        pass


def generate_integer(level):
    if level==1 :
        return random.randint(0,9)

    elif level==2 :
        return random.randint(10,99)

    elif level==3 :
        return random.randint(100,999)

    else :
        get_level()



if __name__ == "__main__":
    main()