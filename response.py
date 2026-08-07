from validator_collection import checkers

def main() :
    user=validate(input("What's your email address? "))
    if user :
        print('Valid')

    else :
        print('Invalid')

def validate(prompt) :
    check=checkers.is_email(prompt)
    return check

if __name__=='__main__' :
    main()