"""
Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of int sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""

def searchRange(nums, target):
    def search(mode):
        resp, left, right = None, 0, len(nums)-1
        while left <= right:
            middle = (left + right)//2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                resp = middle
                if mode:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1 if resp is None else resp
    return [search(False),search(True)]


n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
target = int(input('Target Value to search for: '))

range = searchRange(array, target)
print("Value {} ranges between index {}.".format(target, range))



