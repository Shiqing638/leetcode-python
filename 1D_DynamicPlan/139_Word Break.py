# Methode 1: DFS + memo
# Methode 2: DP
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         wordSet = set(wordDict)
#         memo = {}
#         # from i begin
#         def dfs(i):
#             if i >= len(s):
#                 return True

#             if i in memo:
#                 return memo[i]

#             for word in wordSet:
#                 if s[i:i+len(word)] == word and dfs(i+len(word)):
#                     memo[i] = True
#                     return True
#             memo[i] = False
#             return memo[i]

#         return dfs(0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        #from i begin to seperate
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordSet:
                if s[i: i+len(word)] == word:
                    if dp[i+len(word)]:
                        dp[i] = True
        return dp[0]
