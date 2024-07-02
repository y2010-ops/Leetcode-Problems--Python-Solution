class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {i: nums1.count(i) for i in set(nums1)}
        arr = []
        for val in nums2:
            if val in map1 and map1[val] > 0:
                arr.append(val)
                map1[val] -= 1
        return arr