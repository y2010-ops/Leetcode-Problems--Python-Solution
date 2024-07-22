class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hasho = {}
        for i in range(len(names)):
            hasho[heights[i]] = names[i]
        heights.sort()
        heights = heights[::-1]
        res = []
        for h in heights:
            res.append(hasho[h])
        return res

