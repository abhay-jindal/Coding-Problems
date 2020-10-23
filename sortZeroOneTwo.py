"""
DUTCH NATIONAL FLAG ALGORITHM OR 3-WAY PARTITIONING

There are three indices – low, mid and high. Initially, the value of low = mid = 1 and high = N.

Time Complexity: O(n).
Space Complexity: O(1).
"""

def sortZeroOneTwo(array, n):
   start = 0
   mid = 0
   end = n-1
   while mid <= end:
       if array[mid] == 0:
          array[start], array[mid] = array[mid], array[start]
          start += 1
          mid += 1
       elif array[mid] == 1:
          mid += 1      
       else:
          array[mid], array[end] = array[end], array[mid]
          end -= 1
   return array

n = int(input('Number of elements to be sorted: '))
array = list(map(int,input("\nEnter the elements either 0, 1 or 2: ").strip().split()))[:n] 
print("Array before sorting: {}".format(array))
print("Array after sorting: {}".format(sortZeroOneTwo(array, n)))