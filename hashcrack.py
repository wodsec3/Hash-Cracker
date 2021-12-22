import hashlib

print('''
 _   _           _        ____                _
| | | | __ _ ___| |__    / ___|_ __ __ _  ___| | __
| |_| |/ _` / __| '_ \  | |   | '__/ _` |/ __| |/ /
|  _  | (_| \__ \ | | | | |___| | | (_| | (__|   <
|_| |_|\__,_|___/_| |_|  \____|_|  \__,_|\___|_|\_\
\n\n''')
#=========================================================
# input Hash string 
myhash=input('Give me a Hash: ')
#_________________________________________________________
# A loop for Try to give file path address
while True:
    try:
        # input text file path for cracking hash

        path=input(r'Give me file Path: ')

        file=open(path)

        break

    except FileNotFoundError as e:
        print(str(e), 'file not found!')
#_________________________________________________________-
hashtype=input('''
[1]SHA1
[2]SHA224
[3]SHA256
[4]SHA384
[5]SHA512
[6]SHA3_224
[7]SHA3_256
[8]SHA3_384
[9]SHA3_512
\n Select HASH Type: ''')

# IF AND ELIF FOR SELECT HASH TYPE_________________________+
if hashtype =='1':
    hashobject=hashlib.sha1
elif hashtype =='2':
    hashobject=hashlib.sha224
elif hashtype =='3':
    hashobject=hashlib.sha256
elif hashtype =='4':
    hashobject=hashlib.sha384
elif hashtype =='5':
    hashobject=hashlib.sha512
elif hashtype =='6':
    hashobject=hashlib.sha3_224
elif hashtype =='7':
    hashobject=hashlib.sha3_256
elif hashtype =='8':
    hashobject=hashlib.sha3_384
elif hashtype =='9':
    hashobject=hashlib.sha3_512
#__________________________________________________________+
while True:
    for text in file.readlines():

        striptext=text.strip()

        end=hashobject(striptext.encode())

        if end.hexdigest() == myhash:

            print('[+]HASH FOUND: %s = %s'%(text, myhash))
            break

        else:                                       
            print('[-]HASH NOT FOUND: %s'%(text))              
#___________________________________________________________+
#============================================================



