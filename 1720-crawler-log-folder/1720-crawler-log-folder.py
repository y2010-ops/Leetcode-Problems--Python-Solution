class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = []
        for ops in logs:
            # ops.replace("/", '')
            if ops != "../" and ops != './':
                res.append(ops)
            elif res:
                if ops == "../":
                    res.pop()
                if ops == "./":
                    continue
            else:
                continue
        return len(res)