"""
CONTAINER WITH MOST WATER

https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Time complexity: O(n)
"""

def maxArea(self, height):
    first, second = 0, len(height)-1
    area = 0
    while first <= second:
        area = max(area, min(height[first], height[second]) * (second-first))
        if height[first] < height[second]:
            first += 1
        else:
            second -= 1
    return area


if __name__ == "__main__":
    n = int(input('Number of elements: '))
    array = list(map(int,input("\nEnter the elements: ").strip().split()))[:n]   
    print(f"The max area of water the container can contain is: {maxArea(array)}")