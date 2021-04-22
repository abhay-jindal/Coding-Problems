"""
FIND ALL DUPLICATE NUMBERS IN AN ARRAY

https://leetcode.com/problems/find-all-duplicates-in-an-array/

https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears once or twice, return an array of all the integers that appears twice.

Follow up:

    Could you do it without extra space and in O(n) runtime?

"""

def findDuplicates(nums):
    data = []
    for i in nums:
        if nums[abs(i)-1] < 0:
            data.append(abs(i))
        else:
            nums[abs(i)-1] = -nums[abs(i)-1]
    return data

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print(findDuplicates(array))
