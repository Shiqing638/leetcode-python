import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    c = a + b
                elif token == "-":
                    c = a - b
                elif token == "*":
                    c = a * b
                elif token == "/":
                    c =int(a/b)
                stack.append(c)
        return stack[-1]
        