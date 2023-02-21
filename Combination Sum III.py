k = 3
n = 9
res = []
def backtrack(pos, target, curr):
    if target == 0 and len(curr) == k:
        res.append(curr.copy())
    if target < 0:
        return
    prev = -1
    for i in range(pos, 10):
        if i == prev:
            continue
        curr.append(i)
        # if len(curr) <= k:
        backtrack(i +1, target - i, curr)
        curr.pop()
        prev = i


backtrack(1, n, [])
print(res)