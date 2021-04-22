"""
VALID PERFECT SQUARE 

https://leetcode.com/problems/valid-perfect-square/

Search a sorted array of interval 0 to given num by repeatedly dividing the search interval in half.  
Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, 
narrow the interval to the lower half.  Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).
"""

def isPerfectSquare(num):
   left, right = 0, num
   while left <= right:
      mid = left+(right-left)//2
      if mid**2 == num:
         return mid
      elif mid**2 > num:
         right = mid-1
      else:
         left = mid+1
   return -1

num = int(input('Element to search perfect square of: '))
resp = isPerfectSquare(num)
if resp > 0:
    print("{} is perfect square of {}.".format(num, resp))
else:
    print("{} is not an perfect square.".format(num))
