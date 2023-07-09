# height = [1,8,6,2,5,4,8,3,7]
# Brute Force O(n^2)
# res = 0
# for l in range(len(height)):
#     for r in range(l+1, len(height)):

# O(n)
height = [1, 1]
l = 0
res = 0
r = len(height) - 1
while l < r:
    res = max(res, min(height[l], height[r]) * (r - l))
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(res)