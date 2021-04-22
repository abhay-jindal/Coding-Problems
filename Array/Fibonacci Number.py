"""
FIBONACCI SERIES USING DYNAMIC PROGRAMMING

https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.

"""

def recursiveFibonacci(n, memo = {}):
    if memo.get(n, 0):
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = recursiveFibonacci(n-1, memo) + recursiveFibonacci(n-2, memo)
    return memo[n]

def iterativeFibonacci(n):
    memo = [0,1]
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]


number = int(input("Number to return in fibonacci series: "))
print(iterativeFibonacci(number))
