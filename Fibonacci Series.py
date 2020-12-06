"""
FIBONACCI SERIES USING DYNAMIC PROGRAMMING

space complexity - O(n)

"""

def fibonacci(n, memo = {}):
    print(memo.get(n))
    if memo.get(n, 0):
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


number = int(input("Number to return in fibonacci series: "))
print(fibonacci(number))
