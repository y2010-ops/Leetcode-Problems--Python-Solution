class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root:TreeNode):
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(0, leftmax)
            rightmax = max(0, rightmax)

            # Max path sum with split
            res[0] = max(res[0], root.val + leftmax + rightmax)

#           Max Path sum without split
            return root.val + max(leftmax, rightmax)

        dfs(root)
        return res[0]
    
r = TreeNode(5, 6,7)

print(Solution().maxPathSum(r))

