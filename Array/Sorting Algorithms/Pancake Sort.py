
"""
PANCAKE SORT ALGORITHM

https://leetcode.com/problems/pancake-sorting/

The pancake sort algorithm one by one place maximum element at the end and reduce the size of current array by one. 

Let given array be arr[] of size n. Start from current size equal to n and reduce current size by one while it’s greater than 1. 
Let the current size be curr_size. Do following for every curr_size:
 1. Find index of the maximum element in arr[0..curr_size-1]. Let the index be ‘mi’
 2. Call flip(arr, mi)
 3. Call flip(arr, curr_size-1)

Total O(n) flip operations are performed in above algorithm. The overall time complexity is O(n^2).
"""

# Find maximum element in array[0..n]
def maxElement(array, n):
    max = 0
    for i in range(1, n):
        if array[i] > array[max]:
            max = i
    return max

# Reverses array[0..end]
def flip(array, end):
    start = 0
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

# The main function that sorts given array using flip operations
def pancakeSort(array, n):
    curr_size = n
    while curr_size > 0:
        max = maxElement(array, curr_size)
        if max != curr_size-1:
            if max != 0:
                flip(array, max)
            flip(array, curr_size-1)
        curr_size -= 1
    return array

n = int(input('Number of elements to be sorted: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print("Array before sorting: {}".format(array))
print("Array after sorting: {}".format(pancakeSort(array, n)))