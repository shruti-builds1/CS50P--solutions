import re

def main():
    print(count(input("Text: ")))

def count(s):
    exp=r'(?<![a-z])um(?![a-z])'
    if matches:= re.search(exp, s.strip(), re.IGNORECASE) :
        a, b=re.subn(exp, '*', s, count=0, flags=re.IGNORECASE)
        # print(a)
        return b
    else :
        return 0

if __name__ == "__main__":
    main()