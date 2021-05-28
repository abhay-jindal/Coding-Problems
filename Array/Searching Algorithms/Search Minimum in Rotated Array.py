"""
BINARY SEARCH ALGORITHM

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.
"""


def searchMinValue(nums, start, end):
    if start < end:
        mid = (start+end)//2  # finding middle of the array
        
        # if previous value is greater then current value then definitely current value is smallest
        if nums[mid-1] > nums[mid]:
            return nums[mid]

        # check if array[start ... mid] is sorted or not
        elif nums[mid] > nums[end]:  # if right part [mid, end] is not sorted then value is in right
            return searchMinValue(nums, mid+1, end)
        else:  # if value not in right part then we have to search in left subarray
            return searchMinValue(nums, start, mid-1)
    return nums[start]

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
element = searchMinValue(array, 0, n-1)

print("Minimum Element found: {}".format(element))





