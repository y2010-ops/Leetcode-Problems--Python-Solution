candidates = [10,1,2,7,6,1,5]
target = 8
candidates.sort()
res = []
class Solution:
    def Recursion(self, cur, pos, target):
        if target == 0:
            res.append(cur.copy())
        if target < 0:
            return
        prev = -1
        for i in range(pos, len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            self.Recursion(cur, i + 1, target-candidates[i])
            cur.pop()
            prev = candidates[i]
Solution().Recursion([], 0, target)
print(res)

# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]