class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # DP Method
        dp = [False]*len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for k in range(i-1, -1, -1):
                if nums[k] >= i-k and dp[k] == True:
                    dp[i] = True
                    break
        return dp[-1]
        # # TC: O(n)
        # Greedy Approach
        # farthest = len(nums)-1
        # for i in range(len(nums)-1, -1, -1):
        #     if i + nums[i] >= farthest:
        #         farthest = i
        # if farthest == 0:
        #     return True
        # return False

        

