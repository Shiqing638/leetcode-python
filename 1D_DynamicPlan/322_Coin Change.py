# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         memo = {}

#         def dfs(amount):

#             if amount == 0:
#                 return 0

#             if amount in memo:
#                 return memo[amount]

#             res =  1e9

#             for coin in coins:
#                 if amount - coin >= 0:
#                     res = min(res, 1+ dfs(amount-coin))
#             memo[amount] = res
#             return res


#         minCoin = dfs(amount)

#         return -1 if minCoin >= 1e9 else minCoin
        

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] *(amount+1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        return -1 if dp[amount] == float('inf') else dp[amount]


