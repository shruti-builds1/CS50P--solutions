# user=input('Input: ')
# l=[]
# for k in user :
#     if k.lower() not in 'aeiou' :
#         l.append(k)
# print('Output: \n')
# for i in l :
#     print(i,end='')
# print()

def main():
    user=input('Input: ')
    print('Output:',shorten(user))

def shorten(word):
    s=''
    for k in word :
        if k.lower() not in 'aeiou' :
            s+=k
    return s

if __name__ == "__main__":
    main()
