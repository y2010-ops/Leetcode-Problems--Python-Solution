class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        indx = 0
        total = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                indx = i + 1
        return indx