class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        res = set(arr)
        hash = {}
        for i in res:
            hash[i] = arr.count(i)
        for i in arr:
            if hash[i] == 1:
                count += 1
            if count == k:
                return i
        return ""