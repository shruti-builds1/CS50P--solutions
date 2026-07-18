
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

#TypeError= I don't work with this category of thing at all.
#ValueError= I work with this category fine, but this
#            particular value doesn't make sense here.
