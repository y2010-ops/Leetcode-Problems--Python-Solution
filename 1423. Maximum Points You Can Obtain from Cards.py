nums =  [1,79,80,1,1,1,200,1]
k = 3
l, r = 0, len(nums)-k
total = sum(nums[r:])
res = total

while r < len(nums):
    total += (nums[l]- nums[r])
    res = max(total, res)
    l += 1
    r += 1
print(res)
# arr = []
# l, r = 0, len(nums)-1
# while l<=r:
#     val = max(nums[l], nums[r])
#     arr.append(val)
#     nums[nums.index(val)] = 0
#     l += 1
#     r -= 1
# if len(arr) < k:
#     arr.extend(nums[l:])
# print(arr)
# print(sum(arr[:k]))