class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i:[] for i in range(1, n + 1)}

        def dfs(node, prev):
            if node in visited:
                return True
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    return True
            return False
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

            visited = set()

            if dfs(e1, -1):
                return [e1, e2]
        return []
            