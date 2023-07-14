# O(n) time, O(1) space
s = "AABABBA"
# s = "ABAB"

k = 1
l = 0
# r = 0
res = 0
count = {}
mf = 0
for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    mf = max(mf, count[s[r]])
    length = r-l+1
    if (r-l+1)- mf > k:
        count[s[l]] -= 1
        l += 1
    res = max(res, (r - l + 1))

print(res)

# Time Limit Exceeded
# while l <= r < len(s):
#     hashT = Counter(s[l:r+1])
#     mf = max(hashT.values())
#     if ((r-l + 1) - mf) <= k:
#         res = max(res, ((r-l + 1)))
#         r += 1
#     else:
#         l += 1
# print(res)