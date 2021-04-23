"""
Maximum and minimum of an array using minimum number of comparisons

https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

METHOD : Compare in Pairs

If n is odd then initialize min and max as first element. 
If n is even then initialize min and max as minimum and maximum of the first two elements respectively. 
For rest of the elements, pick them in pairs and compare their maximum and minimum with max and min respectively.

"""

# finding min max through linear search
def findSmallLarge(array):
    n =  len(array)
    small, large = array[0], array[0]
    for i in range(1, n):
        if large < array[i]:
            large = array[i]
        if small > array[i]:
            small = array[i]
    print("Largest element in array is {} and smallest element is {}.".format(large, small))
                      

def findMinMax(nums):
    n = len(array)

    # if nums is even, find min & max from first two elementts 
    if n%2 == 0:
        mn = min(nums[0], nums[1])
        mx = max(nums[0], nums[1])
        index = 2   # starting index of while loop
    else:
        mn = mx = nums[0]  # min & max have same value as that of first index
        index = 1 

    # In the while loop, pick elements in pair and compare the pair with max and min so far
    while index < n-1:
        if nums[index] < nums[index+1]:
            mx = max(mx, nums[index+1])
            mn = min(mn, nums[index])
        else:
            mx = max(mx, nums[index])
            mn = min(mn, nums[index+1])
        index += 2
    print("Largest element in array is {} and smallest element is {}.".format(mx, mn))
    

if __name__ == "__main__":
    n = int(input('Number of elements: '))
    array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n]
    findMinMax(array)


