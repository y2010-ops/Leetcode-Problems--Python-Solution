# Time Complexity = O(n)
nums = [73,74,75,71,69,72,76,73]
# Output -> answer =  [1,1,4,2,1,1,0,0]

# # Brute Force
# res = [0] * len(nums)
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         if nums[j] > nums[i]:
#             res[i] = j - i
#             break
# print(res)

# By Using Stack
ans = [0] * len(nums)
stack = [] # [[index, temp]]

for i, t in enumerate(nums):
    while stack and t > stack[-1][1]:
        index, temp = stack.pop()
        ans[index] = i - index
    stack.append([i,t])
print(stack)
print(ans)

