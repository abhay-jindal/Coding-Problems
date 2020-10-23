"""
KADANE ALGORITHM FOR LARGEST CONTIGUOUS ARRAY SUM

Simple idea of the Kadane’s algorithm is to look for all positive contiguous segments of the array (max_ending_here). 
And keep track of maximum sum contiguous segment among all positive segments (max_so_far). 
Each time we get a positive sum compare it with max_so_far and update max_so_far if it is greater than max_so_far.

Time Complexity: O(n)
Algorithmic Paradigm: Dynamic Programming
"""

def maxSubArraySum(array):
   max_so_far = 0
   max_ending_here = 0
   for i in array:
       max_ending_here += i
       if max_ending_here < 0:
           max_ending_here = 0
       elif max_so_far < max_ending_here:
           max_so_far = max_ending_here
   return max_so_far

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
print("Maximum contiguous sum is {}".format(maxSubArraySum(array)))

