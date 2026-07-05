user=input('File Name : ').lower().strip()
if user.endswith('.gif') :
    print('image/gif')
elif user.endswith('.jpg') or user.endswith('.jpeg') :
    print('image/jpeg')
elif user.endswith('.png') :
    print('image/png')
elif user.endswith('.pdf') :
    print('application/pdf')
elif user.endswith('.txt') :
    print('text/plain')
elif user.endswith('.zip') :
    print('application/zip')
else :
    print('application/octet-stream')
# match user :
#     case user.endswith('.gif') :
#         print('image/gif')
#     case user.endswith('.jpg') | user.endswith('.jpeg') :
#         print('image/jpeg')
#     case user.endswith('.png') :
#         print('image/png')
#     case user.endswith('.pdf') :
#         print('application/pdf')
#     case user.endswith('.txt') :
#         print('txt/plain')
#     case user.endswith('.zip') :
#         print('application/zip')
#     case _:
#         print('application/octet-stream')
