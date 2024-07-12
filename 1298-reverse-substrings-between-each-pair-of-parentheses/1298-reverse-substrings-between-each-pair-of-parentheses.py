class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        q = deque()
        pair = [0] * len(s)
        for p2 in range(len(s)):
            if s[p2] == "(":
                q.append(p2)
            elif s[p2] == ")":
                p1 = q.pop()
                pair[p2] = p1
                pair[p1] = p2

        res = []
        curr_index = 0
        direction = 1

        while curr_index < len(s):
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                res.append(s[curr_index])
            curr_index += direction

        return "".join(res)