from  random import random
# imported random

n=random()*900+100
# random number generated between100 to 900

print(int(n))

a=n//100
a+=(n//10)%10
a+=n%10
# the sum is calculated

print(int(a))
# prints the sum of numbers
