import sys
import pyfiglet
import random

fonts=pyfiglet.FigletFont.getFonts()
if len(sys.argv)==1 :
    rfont=random.choice(fonts)
    user=input('Input: ')
    text1=pyfiglet.figlet_format(user,font=rfont)
    print('Output:')
    print(text1)

elif len(sys.argv)==3 :
    if sys.argv[1] in ('-f','--font') and sys.argv[2] in fonts :
        user=input('Input: ')
        text2=pyfiglet.figlet_format(user,font=sys.argv[2])
        print('Output:')
        print(text2)

    else :
        sys.exit()

else :
    sys.exit()


#  whenever you catch yourself writing \n inside a string 
# and adding more stuff after it with a comma in the same print(),
#  split it into two print() lines instead.

# non-zero exit code = signal that something failed, and passing 
# a message string is the simplest way to guarantee that signal every time.
# sys.exit("some message") = does two things at once:

# Prints that message to the screen (specifically to stderr, the error stream)
# Sends a non-zero exit code automatically — no need to also type a number