import emoji

while True :
    user=input('Input: ')
    output=emoji.emojize(user,language='alias')
    if user==output :
        pass
    else :
        print('Output:',output)
        break

# Think back to what you found earlier about checking
#  whether a string starts/ends with something — 
# that's the tool that would let you add colons only 
# when they're missing, rather than rejecting input 
# that's missing them. Which behavior do you want to build,
#  and do you remember the string methods that would 
# let you check for that?