def DecimalToBinary(num):
   if num > 1 :
       DecimalToBinary(num//2)
   print(num % 2, end = '')

decimal_value = int(input("Please enter the Decimal Number : "))
print(f"The binary equivalent of {decimal_value} is : ")

DecimalToBinary(decimal_value)
print()