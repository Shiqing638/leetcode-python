# Methode 1: DFS + memo
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]

        return dfs(0)

# Methode 2: DP
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+2)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]

        return dp[0]

# Methode 3: DP + op
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 0 #dp[i+2]
        two = 1 # dp[i+1]
        for i in range(n-1, -1, -1):
            tmp = one + two
            one = two
            two = tmp
        return tmp

