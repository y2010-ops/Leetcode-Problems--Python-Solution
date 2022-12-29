
# Brute Force Method

# count = 0
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         if sum(nums[i:j+1]) == k:
#             count += 1
# print(count)

# Good Method
class Solution:
    def subarraySum(self, nums, k: int):
        hashmap = {}
        hashmap[0] = 1
        count = 0
        prfxsum = 0
        for i in range(len(nums)):
            prfxsum += nums[i]
            if prfxsum - k in hashmap:
                count += hashmap[prfxsum - k]

            if prfxsum in hashmap:
                hashmap[prfxsum] += 1
            else:
                hashmap[prfxsum] = 1
        print(count)

Solution().subarraySum([6,4,3,1], 10)

