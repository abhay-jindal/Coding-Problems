"""
Find First and Last Position of Element in Sorted Array

https://www.geeksforgeeks.org/count-number-of-occurrences-or-frequency-in-a-sorted-array/

https://leetcode.com/discuss/interview-question/124724/

Given an array of int sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return 0.

Follow up: Could you write an algorithm with O(log n) runtime complexity?
"""

def countFrequency(nums, target):
    def search(mode):
        resp, left, right = None, 0, len(nums)-1
        while left <= right:
            middle = (left + right)//2

            # if middle element is less then target, then obviously range will start from second half.
            if nums[middle] < target:
                left = middle + 1

            # if middle element is greater then target, then obviously range will end in first second half itself.
            elif nums[middle] > target:
                right = middle - 1

            else:
                resp = middle  # update the resp to middle element.

                # mode is True (for first element of range) search left part only.
                if mode:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1 if resp is None else resp

    # iteratively binary search two times to find the range first by left part and then second part.
    first = search(True)
    if first == -1:
        return 0
    else:
        last = search(False)
        return last + first - 1


n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
target = int(input('Target Value to search for: '))

frequency = countFrequency(array, target)
print("Value {} occurs {} number of times.".format(target, frequency))



