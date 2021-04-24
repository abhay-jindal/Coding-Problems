"""
Maximum Sum Path in Two Arrays

https://leetcode.com/problems/get-the-maximum-score/

https://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/

Given two sorted arrays, such that the arrays may have some common elements. 
Find the sum of the maximum sum path to reach from the beginning of any array 
to end of any of the two arrays. We can switch from one array to another array only at common elements. 

Note: The common elements do not have to be at the same indexes.
Expected Time Complexity: O(m+n), where m is the number of elements in ar1[] and n is the number of elements in ar2[].

"""

def maxSum(nums1, nums2):
    max1, max2 = 0, 0
    i, j = 0, 0
    max_so_far = 0
    n, m = len(nums1), len(nums2)
    while i < n and j < m:

        if nums1[i] > nums2[j]:
            max2 += nums2[j]
            j += 1
        elif nums2[j] > nums1[i]:
            max1 += nums1[i]
            i += 1
        else:
            max_so_far += max(max1, max2)
            max1, max2 = 0, 0
            temp = i
            while i < n and nums1[i] == nums2[j]:
                max1 += nums1[i]
                i += 1
                    
            while j < m and nums1[temp] == nums2[j]:
                max2 += nums2[j]
                j += 1
                    
            max_so_far += max(max1, max2)
            max1, max2 = 0, 0
                  
    for index1 in range(i, n):
        max1 += nums1[index1]
    for index2 in range(j, m):
        max2 += nums2[index2]
     
    max_so_far += max(max1, max2)
    return max_so_far

n = int(input('Number of elements for first array: '))
nums1 = list(map(int,input("\nEnter the elements for first array: ").strip().split()))[:n] 

m = int(input('Number of elements for second array: '))
nums2 = list(map(int,input("\nEnter the elements for second array: ").strip().split()))[:m] 

print(f'The maximum obtained in above two arrays is: {maxSum(nums1, nums2)}')
