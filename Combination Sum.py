candidates = [2, 3, 6, 7]
target = 7
res = []
class Solution:
    candidates = [2, 3, 6, 7]
    target = 7
    res = []
    def dfs(self, i, curr):
        if sum(curr) == target:
            res.append(curr.copy())
            return
        if sum(curr) < target and i < len(candidates):
            curr.append(candidates[i])
            self.dfs(i , curr)
        else:
            return
        curr.pop()
        self.dfs(i+1, curr)

Solution().dfs(0, [])
print(res)