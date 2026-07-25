# user=input('Greeting : ').strip().lower()
# if user.startswith('hello') :
#     print('$0')
# elif user.startswith('h') :
#     print('$20')
# else :
#     print('$100')

def main():
    user=input('Greeting : ')
    print(value(user))

def value(greeting):
    if greeting.lower().startswith('hello') :
        return 0
    elif greeting.lower().startswith('h') :
        return 20
    else :
        return 100

if __name__ == "__main__":
    main()
