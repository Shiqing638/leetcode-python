class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.minStack:
            self.minStack.append(min(value, self.minStack[-1]))
        else:
            self.minStack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        res = self.stack[-1]
        return res

    def getMin(self) -> int:
        return self.minStack.pop()
