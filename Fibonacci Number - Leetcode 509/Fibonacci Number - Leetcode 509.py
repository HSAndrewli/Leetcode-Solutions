# Top Down Recursive

# Time: O(2^n)
# Space: O(n)

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Top Down Memoized

# Time: O(n)
# Space: O(n)

def fib2(n: int) -> int:
    memo = {0:0, 1:1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
    
    return f(n)


# Bottom Up Tabulation

# Time: O(n)
# Space: O(n)

def fib3(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[n]


# Bottom Up Constant Space

# Time: O(n)
# Space: O(1)

def fib4(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    cur = 1

    for i in range(2, n+1):
        prev, cur = cur, prev+cur
    
    return cur

print(fib4(10))
