"""
SELECTION SORT ALGORITHM 

For Reference : https://en.wikipedia.org/wiki/Selection_sort

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
This is an in-place sorting algorithm.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

Auxiliary Space: O(1)
Time Complexity: O(n*n) as there are two nested loops.
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.
"""

def selectionSort(array, n):
   for i in range(n):
      minIndex = i

      # Find the minimum element in remaining unsorted array 
      for j in range(i+1, n):
         if array[minIndex] > array[j]:
            minIndex = j

      # Swap the found minimum element with the first element 
      array[i], array[minIndex] = array[minIndex], array[i]
   return array

n = int(input('Number of elements to be sorted: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print("Array before sorting: {}".format(array))
print("Array after sorting: {}".format(selectionSort(array, n)))
