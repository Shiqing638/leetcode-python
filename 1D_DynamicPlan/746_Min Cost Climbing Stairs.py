# Methode 1: Top down， dfs
# Methode 2: Bottom up， for， iterative
# Methode 3: space optimize
# 1: 从i出发
# class Solution:
#     def minCostClimbingStairs(self, cost: list[i]) -> int:
#         memo = [-1] * len(cost)

#         def dfs(i):
#             if i >= len(cost):
#                 return 0

#             if memo[i] != -1:
#                 return memo[i]

#             memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
#             return memo[i]

#         return min(dfs(0), dfs(1))

#2: 到达i
# class Solution:
#     def minCostClimbingStairs(self, cost: list[i]) -> int:
#         dp = [0] * (len(cost)+1)

#         for i in range(2, len(cost)+1):
#             dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])

#         return dp[len(cost)]

#3
class Solution:
    def minCostClimbingStairs(self, cost: list[i]) -> int:
        prev1 = 0 #dp[1]
        prev2 = 0 #dp[0]

        for i in range(2, len(cost) +1):
            cur = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2 = prev1
            prev1 = cur
        return prev1
