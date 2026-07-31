# Methode 1: brute force
# Methode 2: stack

# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         res = []
#         for i in range(len(temperatures)):
#             found = False
#             for j in range(i+1, len(temperatures)):
#                 if temperatures[j] > temperatures[i]:
#                     res.append(j-i)
#                     found = True
#                     break
#             if not found:
#                 res.append(0)
#         return res

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res 
