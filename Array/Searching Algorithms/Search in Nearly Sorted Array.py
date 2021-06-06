"""
    Search in an almost sorted array

    https://www.geeksforgeeks.org/search-almost-sorted-array/

    Given an array which is sorted, but after sorting some elements are moved to
    either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1]. 
    Write an efficient function to search an element in this array. Basically the element arr[i] 
    can only be swapped with either arr[i+1] or arr[i-1].

    For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved to previous position.

    Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
    Output: 2 
    Output is index of 40 in given array

"""


def searchInSortedArray(nums, k):
    start = 0
    
    end = len(nums)-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == k:
            return mid
        if start < mid and nums[mid-1] == k:
            return mid-1
        if mid < end and nums[mid+1] == k:
            return mid+1
        elif nums[mid] < k:
            start = mid+2
        else:
            end = mid-2 
    return -1

    
n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
k = int(input('Element to search for: '))
index = searchInSortedArray(array, k)

print(f"Element {k} found at index: {index}")





