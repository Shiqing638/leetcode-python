#Methode 1: backtrack


# class Solution:
#     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
#         res = []
#         cur = []

#         def dfs(i, remain):

#             if remain == 0:
#                 res.append(cur.copy())
#                 return

#             if i >= len(candidates) or remain < 0:
#                 return

#             cur.append(candidates[i])
#             dfs(i, remain - candidates[i])
#             cur.pop()
#             dfs(i+1, remain)

#         dfs(0, target)
#         return res

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        cur = []

        def dfs(start, remain):
            if remain == 0:
                res.append(cur.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    continue

                cur.append(candidates[i])
                dfs(i, remain-candidates[i])
                cur.pop()
        dfs(0, target)
        return res




