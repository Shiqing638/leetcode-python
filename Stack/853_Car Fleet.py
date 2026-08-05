class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        car = list(zip(position, speed))
        car.sort(reverse=True)

        stack = []
        for pos, spe in car:
            time = (target - pos) / speed
            stack.append(time)
            if stack[-1] < stack[-2]:
                stack.pop()
        return len(stack)