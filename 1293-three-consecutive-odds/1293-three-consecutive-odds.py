class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def odd(n):
            if n % 2 != 0:
                return True
            else:
                return False
        c = 0
        for val in arr:
            if odd(val):
                c += 1
                if c == 3:
                    return True
            else:
                c = 0    
        return False
        