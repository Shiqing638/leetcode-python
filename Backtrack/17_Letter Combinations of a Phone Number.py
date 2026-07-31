# Methode 1: iterative
# Methode 2: backtrack
#class Solution:
# def letterCombinations(self, digites: str) -> list[str]:
#     dict = {"2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv", 
#             "9": "wxyz"}

#     res = [""]

#     for digit in digites:
#         tmp = []
#         for curStr in res:
#             for c in dict[digit]:
#                 tmp.append(curStr + c)
#         res = tmp
#     return res

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        path = []
        dict = {"2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv", 
                "9": "wxyz"}

        def backtrack(i):
            if i == len(digits):
                res.append("".join(path))
                return

            for c in dict[digits[i]]:
                path.append(c)
                backtrack(i+1)
                path.pop()

        if digits:
            backtrack(0)

        return res


        