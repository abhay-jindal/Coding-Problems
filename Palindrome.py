"""
Program to check if given number is palindrome or not. This can also be used to 
reverse the given number
"""

def reverseDigit(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num = num//10
    return rev

number = int(input('Enter number to check palindrome: '))
reverse = reverseDigit(number)
if number ==  reverse:
    print("{} is an palindrome!".format(number))
else:
    print("{} is not an palindrome!".format(number))
