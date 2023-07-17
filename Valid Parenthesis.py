# Method - 1

class Solution:
    def isValid(self, s: str) -> bool:
        map = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
                continue
            if not stack or stack[-1] != map[c]:
                return False
            stack.pop()

        if not stack: return True

# Method -2
# Naive Approach
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for char in s:
#             if char == '(' or char == '{' or char == '[':
#                 stack.append(char)
#             else:
#                 if not stack:
#                     return False
#                 if char == ')' and stack[-1] == '(':
#                     stack.pop()
#                 elif char == '}' and stack[-1] == '{':
#                     stack.pop()
#                 elif char == ']' and stack[-1] == '[':
#                     stack.pop()
#                 else:
#                     return False
#         return not stack
#         # hashmap = {"(": ")", "{": "}", "[": "]"}
#         # q = collection.deque()
#         # for i in q:
