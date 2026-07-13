def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2<=len(s)<=6 :
        if s[0].isalpha() and s[1].isalpha() :
            if s.isalnum() :
                num=''
                for i in range(len(s)) :
                    if s[i].isdigit() :
                        num=s[i:len(s):1]
                        break
                    else:
                        pass
                if len(num)>0 :
                    if not num.isdigit() or num.startswith('0') :
                        return False
                    else :
                        return True
                else :
                    return True
            else :
                return False              
        else :
            return False
    else :
        return False
        
main()
