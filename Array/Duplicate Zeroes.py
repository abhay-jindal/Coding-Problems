"""
DUPLICATE ZEROES

https://leetcode.com/problems/duplicate-zeros/

Given a fixed length array of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place.

The time complexity of the above algorithm is O(n). 
"""

def duplicateZeroes(array):
   n = len(array)
   zeroesCount = 0
   length_ = n-1
   for left in range(n):
       if left > length_ - zeroesCount:
          break
       if array[left] == 0:
          if left == length_ - zeroesCount:
              array[length_] = 0
              length_ -= 1
              break
          zeroesCount += 1

   newLength_ = length_ - zeroesCount
   for last in range(newLength_, -1, -1):
       if array[last] != 0:
           array[last+zeroesCount] = array[last]
       else:
           array[last+zeroesCount] = 0
           zeroesCount -= 1
           array[last+zeroesCount] = 0
   return array

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print(duplicateZeroes(array))
