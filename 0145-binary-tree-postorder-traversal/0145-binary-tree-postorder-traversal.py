# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        res = []
        x = [root]
        while x:
            node = x.pop()
            res.append(node.val)
            if node:
                if node.left:
                    x.append(node.left)
                if node.right:
                    x.append(node.right)
        return res[::-1]
        

