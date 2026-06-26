def main() :
    line=input('Enter a line : ')
    print(convert(line))

def convert(line) :
    line1=line.replace(':)','🙂')
    line2=line1.replace(':(','🙁')
    return line2

main()

    
