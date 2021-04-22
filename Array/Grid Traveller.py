"""
GRID TRAVELLER PROBLEM

https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the 
bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Time complexity - O(n*m) as we have m number of disticnt choices and n number of disticnt choices
Space complexity - O(n+m)
"""

def gridTraveller(row, column, memo = {}):
    key = "{},{}".format(row, column)
    if memo.get(key, ""):
        return memo[key]
    if row == 0 or column == 0:
        return 0
    elif row == 1 or column == 1:
        return 1
    memo[key] = gridTraveller(row-1, column, memo) + gridTraveller(row, column-1, memo)
    return memo[key]


rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))
print(gridTraveller(rows, columns))
