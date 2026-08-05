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

# class Solution:
#     def minCostClimbingStairs(self, cost: list[i]) -> int:
#         dp = [0] * (len(cost)+2)

#         for i in range(len(cost)-1, -1, -1):
#             dp[i] = min(cost[i]+dp[i+1], cost[i]+dp[i+2])
        
#         return min(dp[0], dp[1])

#3
class Solution:
    def minCostClimbingStairs(self, cost: list[i]) -> int:
        one = 0 # dp[i+1]
        two = 0 # dp[i+2]

        for i in range(len(cost)-1, -1, -1):
            cur = cost[i] + min(one, two)
            two = one
            one = cur
        return min(one, two)