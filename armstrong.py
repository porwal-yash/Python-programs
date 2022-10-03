# Python program to check if the number provided by the user is an Armstrong number or not
# take input from the user
number = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = number
while temp > 0:
digit = temp % 10
sum += digit ** 3
temp //= 10
# display the result
if number == sum:
print(number,"is an Armstrong number")
else:
print(number,"is not an Armstrong number")
