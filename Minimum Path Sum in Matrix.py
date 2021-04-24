"""
MINIMUM PATH SUM IN MATRIX  

https://leetcode.com/problems/minimum-path-sum/

https://www.geeksforgeeks.org/min-cost-path-dp-6/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""

def minPathSum(grid, row=0, column=0):
    row = len(grid)
    column = len(grid[0])
        
    matrix = [[0 for _ in range(column)] for _ in range(row)]    
    matrix[0][0] = grid[0][0]
        
    for i in range(1, row):
        matrix[i][0] = matrix[i-1][0] + grid[i][0]
                 
    for i in range(1, column):
        matrix[0][i] = matrix[0][i-1] + grid[0][i]
            
    # For rest of the 2d matrix
    for i in range(1, row):
        for j in range(1, column):
            matrix[i][j] = grid[i][j] + min(matrix[i - 1][j], matrix[i][j - 1])

            # In case we can move diagonally as well, consider the previous diagonal element
            # matrix[i][j] = grid[i][j] + min(matrix[i - 1][j], matrix[i][j - 1], min[i-1][j-1])

    return matrix[row-1][column-1]


rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))

grid = []
for _ in range(rows):
    grid.append(list(map(int,input("\nEnter the elements: ").strip().split()))[:columns])

print(f"Minimum path sum in given matrix: {}")

