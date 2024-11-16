class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2:
            return nums
        res = []
        for i in range(1, len(nums)-k+2):
            prev = nums[i-1]
            z = [prev]
            n = 1
            while i < len(nums) and nums[i] == prev +1 and n < k:
                z.append(nums[i])
                n += 1
                prev = nums[i]
                i += 1

            if len(z) == k:
                res.append(max(z))
            else:
                res.append(-1)
                
        return res
