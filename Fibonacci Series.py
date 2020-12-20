"""
FIBONACCI SERIES USING DYNAMIC PROGRAMMING

space complexity - O(n)

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
