class Solution:
    def validTree(self, n, edges) -> bool:
        map = {i: [] for i in range(n)}
        if not n:
            return True
        for v1, v2 in edges:
            map[v1].append(v2)
            map[v2].append(v1)

        visited = set()

        def dfs(v, prev):
            if v in visited:
                return False

            visited.add(v)
            for neighbours in map[v]:
                if neighbours == prev:
                    continue
                if dfs(neighbours, v) == False:
                    return False
            return True

        return dfs(0, -1) and n == len(visited)
obj = Solution()
print(obj.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
