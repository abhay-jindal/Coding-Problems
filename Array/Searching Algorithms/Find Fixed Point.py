"""
Find a Fixed Point (Value equal to index) in a given array

https://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/

Given an array of n distinct integers sorted in ascending order, write a function 
that returns a Fixed Point in the array, if there is any Fixed Point present in array, 
else returns -1. Fixed Point in an array is an index i such that arr[i] is equal to i. 
Note that integers in array can be negative. 

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""


# function to return nums index for nums[index] = index
def findIndex(nums, start, end):
    while start <= end:
        middle = (start + end)//2
        if nums[middle] == middle:
            return middle
        elif nums[middle] < middle:
            start = middle+1
        else:
            end = middle-1
    return -1


n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
index = findIndex(array, 0, n-1)
print("Index {} have same value as of array[{}].".format(index, index))


