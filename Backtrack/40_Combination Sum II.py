# Methode 1: backtrack
# Methode 2: for + backtrack
# class Solution:
#     def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
#         res = []
#         cur = []
#         def backtrack(i, summe):
#             if i >= len(candidates):
#                 return []
#             if summe == target:
#                 res.append(cur.copy())
#                 return res
#             cur.append(candidates[i])
#             backtrack(i+1, summe + candidates[i])
#             cur.pop()
#             backtrack(i+1, summe)

#         return backtrack(0, 0)
    
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        cur = []

        def backtrack(i, remain):
            if remain == 0:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or remain < 0:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                cur.append(candidates[j])
                backtrack(j+1, remain - candidates[j])
                cur.pop()
            
        backtrack(0, target)
        return res
