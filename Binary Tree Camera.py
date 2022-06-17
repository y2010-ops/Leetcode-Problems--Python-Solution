class Solution:
    def minCameraCover(self, root: Optional[TreeNode]):
        def postorder(node):
            if not node:
                return (0, math.inf)

            l_count, l_state = postorder(node.left)
            r_count, r_state = postorder(node.right)

            state = min(l_state, r_state)
            total_cameras = l_count + r_count

            if state == 0:
                return (total_cameras + 1, 1)

            if state == 1:
                return (total_cameras, 2)

            return (total_cameras, 0)

        dummy = TreeNode(-1, root)

        return postorder(dummy)[0]

s = Solution()
print(s.minCameraCover([0, 0, null, 0, 0]))