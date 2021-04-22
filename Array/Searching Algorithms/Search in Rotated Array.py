"""
BINARY SEARCH ALGORITHM

https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
"""


def searchInRotatedArray(array, start, end, key):
    if start <= end:
        mid = (start+end)//2  # finding middle of the array
        
        if array[mid] == key:  # if middle elemnt value is key then return middle
            return mid

        # check if array[start ... mid] is sorted or not
        if array[start] <= array[mid]:

            # if key is within confined range then search left part of array else right part
            if array[start] <= key <= array[mid]:
                return searchInRotatedArray(array, start, mid-1, key)
            return searchInRotatedArray(array, mid+1, end, key)

        # if array[start ... mid] is not sorted, then definitely array[mid+1 ... end] is sorted
        if array[mid] <= key <= array[end]:
            return searchInRotatedArray(array, mid+1, end, key)
        return searchInRotatedArray(array, start, mid-1, key)
    return -1

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
searchElement = int(input('Element to search: '))
element = searchInRotatedArray(array, 0, n-1, searchElement)

if element > 0:
    print("Element found at {} index".format(element))
else:
    print("Element cannot be found in array.")




