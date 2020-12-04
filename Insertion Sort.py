
"""
INSERTION SORT

The insertion sort algorithm picks values from the unsorted part and places them at correct position in the sorted part.

Time Complexity: O(n*2)
Auxiliary Space: O(1)
Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. 
And it takes minimum time (Order of n) when elements are already sorted.

Algorithmic Paradigm: Incremental Approach
Sorting In Place: Yes
Stable: Yes
Online: Yes
Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, 
only few elements are misplaced in complete big array.
"""


def insertionSort(array, n):
    for i in range(1, n):
        j = i-1

        # Move elements of arr[1..n], that are 
        # greater than next element, to one position ahead 
        # of their current position 
        while j >= 0 and array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
    return array


n = int(input('Number of elements to be sorted: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print("Array before sorting: {}".format(array))
print("Array after sorting: {}".format(insertionSort(array, n)))





