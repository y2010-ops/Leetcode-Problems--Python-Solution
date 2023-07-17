# Method - 1
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        res = [-1, -1]
        length = float("infinity")
        hash_t = {}
        hash_win = {}
        for r in t:
            hash_t[r] = 1 + hash_t.get(r, 0)
            hash_win[r] = 0
        need = len(hash_t)
        have = 0
        l = 0
        for r in range(len(s)):
            if s[r] in t:
                hash_win[s[r]] += 1
                if hash_win[s[r]] == hash_t[s[r]]:
                    have += 1
            while have == need:
                curr_len = r-l+1
                if curr_len < length:
                    res = [l,r]
                    length = r-l + 1

                if s[l] in t:
                    hash_win[s[l]] -= 1
                    if hash_win[s[l]] < hash_t[s[l]]:
                        have -= 1

                l += 1
        l, r = res
        return s[l:r+1] if length != float("infinity") else ""

# Method - 2
# hash_t, hash_win = defaultdict(int), defaultdict(int)

# for r in t:
#     hash_t[r] += 1

# have, need = 0, len(hash_t)
# res, length = [-1, -1], float("infinity")
# l = 0
# for r in range(len(s)):
#     hash_win[s[r]] += 1
#     if s[r] in t and hash_t[s[r]] == hash_win[s[r]]:
#         have += 1

#     while need == have:
#         currlen = r-l+1
#         if currlen < length:
#             res = [l, r]
#             length = r-l + 1
#         hash_win[s[l]] -= 1
#         if s[l] in t and hash_win[s[l]] < hash_t[s[l]]:
#             have -= 1

#         l += 1
# l, r = res
# return s[l:r+1] if length != float("infinity") else ""
