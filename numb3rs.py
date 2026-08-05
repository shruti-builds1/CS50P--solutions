import re
# from validator_collection import checkers

def main():
    user=validate(input("IPv4 Address: "))
    if user :
        print('True')
    else :
        print('False')


def validate(ip):

    exp=re.compile(r'''^(([0-9]|[1-9][0-9]|[1-2][0-4][0-9]|[1][5-9][0-9]|
    [2][5][0-5]))\.(([0-9]|[1-9][0-9]|[1-2][0-4][0-9]|[1][5-9][0-9]|
    [2][5][0-5]))\.(([0-9]|[1-9][0-9]|[1-2][0-4][0-9]|[1][5-9][0-9]|
    [2][5][0-5]))\.(([0-9]|[1-9][0-9]|[1-2][0-4][0-9]|[1][5-9][0-9]|
    [2][5][0-5]))$''', re.VERBOSE)
    if matches:= exp.search(ip.strip()) :
        # print(matches.group())
        a, b, c, d = matches.group().split('.')
        if int(a)<= 255 and int(b)<= 255 and int(c)<= 255 and int(d)<= 255:
            return True
        else :
            return False
    else :
        return False

# def validate(ip):
#     check=checkers.is_ipv4(ip)
#     return check

if __name__ == "__main__":
    main()

# this library only handles "is this a generally valid X"
# it can't be customized to enforce an assignment-specific extra rule 
# like "no leading zeros allowed"
# unless the library happens to expose that as a specific option
# i.e., strict parameter