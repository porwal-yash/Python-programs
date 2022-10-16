import random
# imports random package
reference_string="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#_&-+()/?!;:"
# this is a reference string which would be used as password

size=int(input("Enter the size of password you want: "))
# input the size as integer

password="".join(random.sample( reference_string , size))
# this will join the string with random string having size specified by user

print ('\n\t',password)
# outputs passwords
