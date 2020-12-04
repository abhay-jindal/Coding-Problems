
"""
INSERTION SORT

The insertion sort algorithm picks values from the unsorted part are picked and placed at the correct position in the sorted part
Algorithms assign values instead of swapping them which makes it faster.
Reference - https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/SortOpt.html#code-tuning-for-simple-sorting-algorithms

Time Complexity: O(n*2)
Auxiliary Space: O(1)

Sorting In Place: Yes
"""


def insertionSort(array, n):
    for i in range(1, n):

        # Assign elements of arr[1..n], that are 
        # greater than next element, to one position ahead 
        # of their current position 
        temp = array[i]
        while i > 0 and temp < array[i-1]:
            array[i] = array[i-1]
            i -= 1
        array[i] = temp
    return array


n = int(input('Number of elements to be sorted: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print("Array before sorting: {}".format(array))
print("Array after sorting: {}".format(insertionSort(array, n)))





