import collections
# t =  [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
# graph = collections.defaultdict(list)
# for i in range(len(t)):
#     graph[i] = t[i]
# print(graph)

def dfs(visited, path, node, graph):
        dest = len(graph) - 1
        if node == dest:
            visited.append(path)
        for neighbours in graph[node]:
            dfs(visited, path+[neighbours], neighbours, graph)

visited = []
graph = collections.defaultdict(list)
t =  [[4,3,1],[3,2,4],[3],[4],[]]
for i in range(len(t)):
    graph[i] = t[i]

dfs(visited, [0], 0, graph)

print(visited)
