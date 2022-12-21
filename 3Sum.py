# Time Complexity = O(n^2) + O(n logn) = O(n^2)
nums = [-1,0,1,0]
# Output: [[-1,-1,2],[-1,0,1]]
ans = []
nums.sort()
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    l, r = i+1, len(nums)-1
    while l<r:
        threesum = nums[i] + nums[l] + nums[r]
        if threesum > 0:
            r -= 1
        elif threesum < 0:
            l += 1
        else:
            ans.append([nums[i], nums[l], nums[r]])
            l += 1
            while nums[l] == nums[l-1] and l<r:
                l += 1

# we don't have
print(ans)