class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        curGas = 0
        answer = 0
        for j in range(len(gas)):
            totalGas += gas[j] - cost[j]
            curGas += gas[j] - cost[j]
            if curGas < 0:
                curGas = 0
                answer = j + 1
        return answer if totalGas >= 0 else -1