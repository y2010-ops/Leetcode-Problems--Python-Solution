class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            s = 0
            for k in range(i, len(nums)):
                s += nums[k]
                res.append(s)

        res.sort()
        return sum(res[left-1: right])% (10**9 + 7)
