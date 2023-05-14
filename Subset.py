import collections

nums = [1,2,3]
# ---------------------------------------------------------------------------
# Recursion DFS-1
# ---------------------------------------------------------------------------
# res = []
# subset = []
# def dfs(i):
#     if i >= len(nums):
#         res.append(subset.copy())
#         return
#     subset.append(nums[i])
#     dfs(i+1)
#
#     subset.pop()
#     dfs(i+1)
# dfs(0)
# print(res)
# ------------------------------------------------------------------------------
# DFS Recursion-2
# ------------------------------------------------------------------------------
class Solution:
	def subsets(self, nums):
		result = []

		def dfs(subset = [], index = 0):

			if index == len(nums):
				result.append(subset)
				return

			dfs(subset + [nums[index]], index + 1)
			dfs(subset, index + 1)

		dfs()
		print(result)

print(Solution().subsets([1,2,3]))


# ----------------------------------------------------------------------------
# Recursion BFS
# ----------------------------------------------------------------------------
# class Solution:
# 	def subsets(self, nums):
# 		queue = collections.deque([])
#
# 		for i in range(len(nums)):
# 			queue.append(([nums[i]], i))
#
# 		print(self.bfs(queue, nums))
#
# 	def bfs(self, queue, nums):
# 		result = [[]]
# 		while queue:
# 			curPath, idx = queue.popleft()
#
# 			result.append(curPath)
#
# 			for i in range(idx+1, len(nums)):
# 				queue.append((curPath + [nums[i]], i))
#
# 		print(result)
#
# obj = Solution()
# print(obj.subsets([1,2,3]))

#