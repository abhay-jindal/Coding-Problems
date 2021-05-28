"""
Pow(x, n)

https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000

The idea of binary search is to use the informat.
"""

def myPow(x, n):
   return computeMyPow(x, n) if n >= 0 else 1/computeMyPow(x, abs(n))

def computeMyPow(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n%2 == 0:
        return computeMyPow(x*x, n/2)
    return x * computeMyPow(x*x, n//2)


x = float(input('Number to compute power of: '))
n = int(input('Power to raise: '))
resp = myPow(x, n)

print(f"{x} raise to the power {n} is {resp}.")

