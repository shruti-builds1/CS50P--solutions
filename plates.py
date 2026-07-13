def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")       # none counts in falsy 


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
                    if not num.isdigit() or num.startswith('0') :  # isalnum() checks if the string contains both digits and letters
                        return False                               # isdigit() checks if the string contains digits only
                    else :                                         # isalpha() checks if the string contains letters only
                        return True                                # earlier didn't mention this statement which resulted in none instead of True 
                else :
                    return True                                    # this is for if the string contains only letters 
            else :
                return False              
        else :
            return False
    else :
        return False
        
main()
