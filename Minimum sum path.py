class Solution:
    def minimumTotal(self, triangle):
        dp = [0] * (len(triangle) + 1)

        for x in triangle[::-1]:
            for i, n in enumerate(x):
                dp[i] = n + min(dp[i], dp[i + 1])
        return dp[0]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
s = Solution()
print(s.minimumTotal(triangle))