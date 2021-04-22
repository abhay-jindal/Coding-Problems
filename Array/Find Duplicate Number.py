"""
FIND THE DUPLICATE NUMBER

https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Follow up:

    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem without modifying the array nums?
    Can you solve the problem using only constant, O(1) extra space?
    Can you solve the problem with runtime complexity less than O(n2)?

"""

def findDuplicate(nums):
    for i in nums:
        if nums[abs(i)-1] >= 0:
            nums[abs(i)-1] = -nums[abs(i)-1]
        else:
            return abs(i)

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print(findDuplicate(array))
