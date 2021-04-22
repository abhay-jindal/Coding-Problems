"""
Shortest Unsorted Continuous Subarray

https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array nums, you need to find one continuous subarray that if you only sort
this subarray in ascending order, then the whole array will be sorted in ascending order.
Examples: 
1) If the input array is [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60], the subarray lies between the indexes 3 and 8.
2) If the input array is [0, 1, 15, 25, 6, 7, 30, 40, 50], the subarray lies between the indexes 2 and 5.

Return the shortest such subarray and output its length.

Reference for algorithm: https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
Time Complexity : O(n)

"""


def findUnsortedSubarray(array):
    n = len(nums)
        
    # find first break from start
    start = 0
    while start < n - 1 and nums[start] <= nums[start + 1]:
        start += 1
            
    # already sorted, not subarray sorting needed
    if start == n - 1: return 0
        
    # find first break from end
    end = n - 1
    while end > 0 and nums[end - 1] <= nums[end]:
        end -= 1
        
    # find min/max in [start, end] range
    min, max = nums[start], nums[start]
    for i in range(start, end + 1):
        if nums[i] > max:
            max = nums[i]
        if nums[i] < min:
            min = nums[i]
                      
    # move start back if element found less than min, then break
    while start >= 0 and nums[start] > min:
        start -= 1
        
    # move end forward if element found greater than max, then break
    while end < n and nums[end] < max:
        end += 1
    return end - start - 1


if __name__ == "__main__":
    n = int(input('Number of elements: '))
    array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
   
    length = findUnsortedSubarray(array)
    if length > 0:
       print("Shortest such subarray length to make whole array sorted: {}".format(length))
    else:
       print("Array is already sorted.")
