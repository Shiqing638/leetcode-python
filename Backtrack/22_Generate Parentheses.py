class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        cur = []

        def backtrack(left, right):
            if left == n and right == n:
                res.append("".join(cur))
                return

            if left < n:
                cur.append("(")
                backtrack(left+1, right)
                cur.pop()

            if right < n:
                cur.append(")")
                backtrack(left, right+1)
                cur.pop()

        backtrack(0,0)
        return res

            

