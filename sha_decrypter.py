from hashlib import sha256
from termcolor import colored

hash_value = input("Enter the hash value(sha256):")

HASH = input('[+] Enter Password File To Use: ')
with open(HASH, 'r') as passwords:
    for password in HASH:
        password = password.strip()
        print(colored(('Trying: ' + password), 'red'))

flag = False
val = ""
for word in HASH:
    value = sha256(word.encode())
    if hash_value == value.hexdigest():
        flag = True
        val = word
        break

if flag:
    print("The decrypted word is " + val)

else:
    print("Can't Find")

        #word(str(hash_value, value))

    #5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
    #C:\Users\ankit\PycharmProjects\PYPrograms\NEW PROGRAMS\HASH.txt