class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        hash = []
        for i in range(len(nums)):
            intg = str(nums[i])
            formed = ""
            for val in range(len(intg)):
                formed = formed + str(mapping[int(intg[val])])
            q = int(formed)
            hash.append([q, i])
        hash.sort()
        res = []
        for x in hash:
            res.append(nums[x[1]])
        return res