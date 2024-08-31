
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dist = [0] * n
        dist[start] = 1
        
        for i in range(n - 1):
            updated = False
            for k in range(len(edges)):
                u, v = edges[k]
                pathProb = succProb[k]
                if dist[u] * succProb[k] > dist[v]:
                    dist[v] = dist[u] * succProb[k]
                    updated = True
                if dist[v] * succProb[k] > dist[u]:
                    dist[u] = dist[v] * succProb[k]
                    updated = True
            if not updated:
                break
        
        return dist[end]