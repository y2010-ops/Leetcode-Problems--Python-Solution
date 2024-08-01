class Solution:
    def countSeniors(self, details: List[str]) -> int:
        q = 60
        count = 0
        for info in details:
            age = int(info[11:13])
            if age > q:
                count += 1
            else:
                continue
        return count