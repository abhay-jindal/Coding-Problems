"""
BINARY SEARCH ALGORITHM

https://www.geeksforgeeks.org/find-closest-number-array/

Given an array of sorted integers. We need to find the closest value to the given number. 
Array may contain duplicate values and negative numbers.

The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Logn).
"""


def closestNumberArray(array, start, end, target):

    #corner cases to be checked first
    if array[start] >= target:
        return array[start]
    elif  array[end] <= target:
        return array[end]

    data, index = target, start
    while start <= end:
        mid = start+(end-start)//2

        # update data and index if (current value - target) is less then target itself
        if abs(array[mid]-target) < data:
            data, index = abs(array[mid]-target), mid
           
        if array[mid] < target:    # If target is greater than array element, then search in right
            start = mid+1
        else:                      # If target is less than array element, then search in left
            end = mid-1
    return array[index]


if __name__ == "__main__":
    n = int(input('Number of elements: '))
    array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
    searchElement = int(input('Element to search: '))

    element = closestNumberArray(array, 0, n-1, searchElement)
    print("Closest element found is {}".format(element))