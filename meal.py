# 24 hour format
def main():
    user=input('What time is it? [24-hour format]').lower().strip()
    if 7<= convert(user) <= 8 :
        print('breakfast time')
    elif 12<= convert(user) <= 13 :
        print('lunch time')
    elif 18<= convert(user) <= 19 :
        print('dinner time')
    else :
        pass

def convert(time):
    l=time.split(':')
    result=float(l[0]) + int(l[1])/60
    return result

if __name__ == "__main__":
    main()

# # 12 hour format
# def main():
#     user=input('What time is it? [12-hour format]').lower().strip()
#     if user.endswith('a.m.') :
#         if 7<= convert(user) <= 8 :
#             print('breakfast time')
#         else :
#             pass
#     elif user.endswith('p.m.') :
#         if 12<= convert(user) <= 13 :
#             print('lunch time')
#         elif 18<= convert(user) <= 19 :
#             print('dinner time')
#         else :
#             pass
#     else :
#         pass

# def convert(time):
#     if time.endswith('a.m.') :
#         l=time.rstrip('a.m.').split(':')
#         result=float(l[0]) + int(l[1])/60
#         return result
#     elif time.endswith('p.m.') :
#         l=time.rstrip('p.m.').split(':')
#         if 11>=int(l[0])>=1 :
#             result=float(l[0]) + 12.0 + int(l[1])/60
#             return result
#         else :
#             result=float(l[0]) + int(l[1])/60
#             return result
        
# if __name__ == "__main__":
#     main()