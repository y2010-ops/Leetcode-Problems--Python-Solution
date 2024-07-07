class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalB = numBottles

        while numBottles >= numExchange:

            totalB += int(numBottles//numExchange)
            oddB = numBottles % numExchange
            fullB = int((numBottles - oddB)//numExchange)
            numBottles = fullB + oddB
            # emptyB = numBottles

        return totalB
