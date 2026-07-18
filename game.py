
import random
while True :
    try:
        user1=int(input('Level: '))
        if user1<0 :
            continue
        else :
            guess=random.randint(1,user1)
            while True :
                try :
                    user2=int(input('Guess: '))
                    if user2<0 :
                        continue
                    else :
                        if user2<guess :
                            print('Too small!')
                            continue
                        elif user2>guess :
                            print('Too large!')
                            continue
                        else :
                            print('Just right!')
                            break


                except ValueError :
                    continue
            
            break

    except ValueError :
        continue