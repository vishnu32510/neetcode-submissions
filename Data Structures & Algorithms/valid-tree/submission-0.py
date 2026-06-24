class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {c:[] for c in range(n)}
        seen = set()

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        def dfs(node, prev):
            if node in seen:
                return False
            seen.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(seen) == n
            