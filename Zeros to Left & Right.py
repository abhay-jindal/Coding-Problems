"""
MOVE ZEROES TO LEFT AND RIGHT IN ARRAY

Time complexity: O(n)
"""

def zerosToRight(nums, n):
    start = -1
    for i in range(n):
        if nums[i] == 0:
            if start < 0:
                start = i
            else:
                continue
        elif start >= 0:
            nums[start] = nums[i]
            nums[i] = 0
            start += 1
    return nums

def zerosToLeft(nums, n):
    last = -1
    for i in range(n-1, -1, -1):
        if nums[i] == 0:
            if last < 0:
                last = i
            else:
                continue
        elif last >= 0:
            nums[last] = nums[i]
            nums[i] = 0
            last -= 1
    return nums

if __name__ == "__main__":
    n = int(input('Number of elements: '))
    array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n] 
    print(f"Array after moving all zeroes to left: {zerosToLeft(array, n)}")    
    print(f"Array after moving all zeroes to right: {zerosToRight(array, n)}")