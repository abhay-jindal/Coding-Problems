"""
BINARY SEARCH ALGORITHM

https://leetcode.com/problems/binary-search/

Search a sorted array by repeatedly dividing the search interval in half.  
Begin with an interval covering the whole array. 
If the search key is less than middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. 
Repeatedly check until the value is found or the interval is empty.

The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Logn).
"""


def binarySearch(array, start, end, searchElement):
   if start <= end:
      mid = start+(end-start)//2
      if array[mid] == searchElement:
         return mid
      elif searchElement > array[mid]:
         return binarySearch(array, mid+1, n, searchElement)
      else:
         return binarySearch(array, start, mid-1, searchElement)
   return -1


if __name__ == "__main__":
    n = int(input('Number of elements: '))
    array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
    searchElement = int(input('Element to search: '))
    element = binarySearch(array, 0, n-1, searchElement)

    if element > 0:
       print("Element found at {} index".format(element))
    else:
       print("Element cannot be found in array.")
