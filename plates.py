def main():
    plate = input("Plate: ")
    if is_valid(plate)==False:
        print("Invalid")
    else:
        print("Valid")


def is_valid(s):
    if 2<=len(s)<=6 :
        if s[0].isalpha() and s[1].isalpha() :
            l=[]
            num=''
            # for k in s:
            #     if k in '0123456789' :
            #         l.append(int(k))
            #     else :
            #         l.append(k)
            for i in range(len(s)) :
                if s[i].isdigit() :
                    num=s[i:len(s):1]
                    break
                elif s[i].isalpha() :
                    pass
                else:
                    return False
            if len(num)>0 :
                if num.isalnum() and num.startswith('0') :
                    return False
        else :
            return False
    else :
        return False
        
main()


    # # l=[]
    # # for k in s :
    # #     l.append(k)
    # found=0
    # num=[]
    # letter=[]
    # char=[]
    # if 2<=len(s)<=6 :

    #     if  s[0].isalpha()==True and s[1].isalpha()==True :

    #         for k in s :
    #             if k in ('0','1','2','3','4','5','6','7','8','9') :
    #                 char.append(int(k))
    #             else :
    #                 char.append(k)
            
    #         # if char[0].isalpha()==True and char[1].isalpha()==True :
    #         for i in char :
    #             if i.isalpha()==True :
    #                 letter.append(i)
    #                 if len(num)>0 :
    #                     if len(letter)>limit :
    #                         found+=1

    #             elif i.isdigit()==True :
    #                 num.append(i)
    #                 limit=len(letter)
    #                 if num[0]==0 :
    #                     found+=1

    #             elif found>0 :
    #                 return False
                    
    #             else :
    #                 return False

    #         # else :
    #         #     return False
            
    #     else :
    #         return False

    # else :
    #     return False    
    #         # num=[]
    #         # letter=[]
    # #         for k in s :
    # #             if k.isalpha()==True :
    # #                 letter.append(k)
    # #                 if len(num)>0 :
    # #                     if len(letter)>limit :
    # #                         found+=1
    # #                         # return False
    # #                 #     else :
    # #                 #         return True
    # #                 # else :
    # #                 #     pass
                        
                        
                    
    # #             elif k.isdigit()==True :
    # #                 num.append(k)
    # #                 limit=len(letter)
    # #                 if num[0]=='0' :
    # #                     found+=1
    # #                     # return False
    # #                 # else :
    # #                 #     return True
                     
    # #             elif found>0 :
    # #                 return False
                    

    # #             else :
    # #                 return False
            
                 

    # #     else :
    # #         return False
    # # else :
    # #     return False