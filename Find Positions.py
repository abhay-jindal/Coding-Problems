"""
Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of int sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""

def searchRange(nums, target):
    def search(mode):
        res,l,r=None,0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                res=m
                if mode:
                    l=m+1
                else:
                    r=m-1
        return -1 if res is None else res
    return [search(0),search(1)]

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
target = int(input('Target Value to search for: '))
print(searchRange(array, target))
