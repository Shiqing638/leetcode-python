# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         memo = {}

#         def dfs(i, money):
#             if money == amount:
#                 return 1
            
#             if money > amount:
#                 return 0

#             if i >= len(coins):
#                 return 0

#             if (i, money) in memo:
#                 return memo[(i, money)]

#             memo[(i, money)] = dfs(i, money + coins[i]) + dfs(i+1, money)
#             return memo[(i, money)]

#         return dfs(0, 0)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                if coin > i:
                    continue
                else:
                    dp[i] += dp[i-coin] 
        return dp[amount]