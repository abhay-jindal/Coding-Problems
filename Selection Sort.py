"""
SELECTION SORT

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
This is an in-place sorting algorithm.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

Auxiliary Space: O(1)
Time Complexity: O(n2) as there are two nested loops.
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.
"""

def selectionSort(array):
   for i in range(len(array)):
      minIndex = i

      # Find the minimum element in remaining unsorted array 
      for j in range(i+1, len(array)):
         if array[minIndex] > array[j]:
            minIndex = j

      # Swap the found minimum element with the first element 
      array[i], array[minIndex] = array[minIndex], array[i]
   return array

n = int(input('Number of elements to be sorted: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print("Array before sorting: {}".format(array))
print("Array after sorting: {}".format(selectionSort(array)))
