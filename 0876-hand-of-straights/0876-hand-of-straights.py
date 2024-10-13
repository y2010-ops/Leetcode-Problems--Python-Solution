class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hash = defaultdict(int)
        for i in hand:
            hash[i] += 1
        
        minH = list(hash.keys())
        heapq.heapify(minH)
        while minH:
            val = minH[0]
            for i in range(val, val + groupSize):
                if i not in minH:
                    return False
                hash[i] -= 1
                if hash[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

        