# Combination
n = 4
k = 2
res = []
def dfs(start, curr):
    if len(curr)== k:
        res.append(curr.copy())
        return
    for i in range(start, n+1):
        curr.append(i)
        dfs(i+1, curr)

        curr.pop()



dfs(1, [])
print(res)
