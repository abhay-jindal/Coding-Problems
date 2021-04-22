"""
BUBBLE SORT ALGORITHM

For reference: https://en.wikipedia.org/wiki/Bubble_sort

The bubble sort algorithm sorts an array by repeatedly swapping the adjacent element if they are in wrong order
and pushing the largest element at the end of array on every iteration.
This is an in-place sorting algorithm.

Auxiliary Space: O(1)
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.
Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

"""

def bubbleSort(array):
    n = len(array)

   # Traverse through all array elements 
    for i in range(n):
        swapped = False

        # Last ith element is already in place
        for j in range(n-i-1):

             # traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element 
             if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True  # (1) this means one or more elements were in wrong order i.e. given array is not already sorted.
        if not swapped:
            break  # if condition (1) block is not executed that means array is already sorted so no need to check further elements.
    return array

n = int(input('Number of elements to be sorted: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print("Array before sorting: {}".format(array))
print("Array after sorting: {}".format(bubbleSort(array)))
