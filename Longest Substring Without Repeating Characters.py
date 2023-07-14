# s = "abcabcbb"
# s = "bbbbb"
# s = ""
s = "pwwkew"
# s = "dvdf"
# s = "jlygy"
# # print(len(s))
# ---------------M-1
# res = 0
# a = []
# i = 0
# prev = -1
# while i < len(s):
#     if s[i] not in a:
#         a.append(s[i])
#     else:
#         # res = max(res,len(a))
#         val = s[i]
#         if prev == s[i]:
#              a.clear()
#         else:
#             x = a.index(val)
#             del a[:x+1]
#         a += s[i]
#     res = max(res, len(a))
#     prev = s[i]
#     i += 1
# print(res)

# -----------Sliding Window--------------M-2
l = 0
res = 0
a = set()
for r in range(len(s)):
    if s[r] not in a:
        a.add(s[r])
    else:
        while s[r] in a:
            a.remove(s[l])
            l += 1
        a.add(s[r])
    res = max(res, r - l + 1)

# for r in range(len(s)):
#     while s[r] in a:
#         a.remove(s[l])
#         l += 1
#     a.add(s[r])
#     res = max(res, r - l + 1)

print(res)