class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s, 0)}
        ans = []
        start, end = 0, 0
        for i, c in enumerate(s,0):
            end = max(last[c], end)
            if i == end:
                ans.append(end-start + 1)
                start = end + 1
        return ans