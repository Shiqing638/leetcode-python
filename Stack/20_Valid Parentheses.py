class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in closeToOpen:
                if not stack or stack.pop() != closeToOpen[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
