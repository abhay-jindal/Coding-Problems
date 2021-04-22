"""
REVERSAL ALGORITHM FOR ARRAY ROTATION

https://leetcode.com/problems/rotate-array/

Let AB are the two parts of the input array where A = arr[0..d-1] and B = arr[d..n-1]. The idea of the algorithm is : 
 
Reverse A to get ArB, where Ar is reverse of A.
Reverse B to get ArBr, where Br is reverse of B.
Reverse all to get (ArBr) r = BA.

Time Complexity : O(n)
"""


# Function to reverse array[] from index start to end
def reverseArray(array, start, end):
   while start < end:
      array[start], array[end] = array[end], array[start]
      start += 1
      end -= 1


# Function to left rotate array[] of size n by k
def leftRotateArray(array, k):
   if k ==0:
      return 
   k = k % len(array)   # in case the rotating factor is greater than array length
   reverseArray(array, 0, k-1)
   reverseArray(array, k, n-1)
   reverseArray(array, 0, n-1)
   return array

# Function to right rotate array[] of size n by k
def rightRotateArray(array, k):
   if k ==0:
      return 
   k = k % len(array)   # in case the rotating factor is greater than array length
   reverseArray(array, 0, n-1)
   reverseArray(array, 0, k-1)
   reverseArray(array, k, n-1)
   return array

n = int(input('Number of elements: '))
array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
rotateFactor = int(input('Rotate array by: '))
print("Array before left rotation by factor of {}: {}".format(rotateFactor, array))

print("Array after left rotation by factor of {}: {}".format(rotateFactor, leftRotateArray(array, rotateFactor)))

print("Array after right rotation by factor of {}: {}".format(rotateFactor, rightRotateArray(array, rotateFactor)))
