# Python program to check if the input number is odd or even.
# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.

num = int(input("enter a number:"))
if  (num % 2) == 0:
    print ("{0} is even".format(num))
else:
    print("{0} is odd".format (num))
