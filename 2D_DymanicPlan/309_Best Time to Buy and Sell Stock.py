# Methode 1: DFS + memo
# Methode 2: bottom up
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         buy = True
#         memo = {}

#         def dfs(i, buy):
#             if i >= len(prices):
#                 return 0
#             if (i, buy) in memo:
#                 return memo[(i, buy)]

#             if buy:
#                 memo[(i, buy)] = max(dfs(i+1, False) -prices[i], dfs(i+1, True))
#             else:
#                 memo[(i, buy)] = max(dfs(i+2, True) + prices[i] , dfs(i+1, False))
#             return memo[(i, buy)]

#         return dfs(0, True)

#2:

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices)+1)]
        
        #从第 i 天开始，在 buy 状态下，以后能够获得的最大利润。

        for i in range(len(prices)-1, -1, -1):
            for buy in [True, False]:
                if buy:
                    buying = dp[i+1][False] - prices[i] if i+1<len(prices) else -prices[i]
                    cooldown = dp[i+1][True] if i+1<len(prices) else 0
                    dp[i][1] = max(buying, cooldown)
                else:
                    selling = dp[i+2][True] + prices[i] if i+2 < len(prices) else prices[i]
                    cooldown = dp[i+1][False] if i+1 <len(prices) else 0
                    dp[i][0] = max(selling, cooldown)
        return  dp[0][1]

