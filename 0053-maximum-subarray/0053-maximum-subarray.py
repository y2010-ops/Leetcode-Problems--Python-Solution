class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 3 and sum(nums) < 0:
            return max(nums)
        
        s = 0
        best = -10000
        for i in range(len(nums)):
            s = max(nums[i], s + nums[i])
            best = max(best, s)
        return best