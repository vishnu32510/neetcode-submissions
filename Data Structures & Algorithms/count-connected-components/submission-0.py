class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
            return
        
        com_num = 0
        for i in range(n):
            if i not in visited:
                com_num += 1
                dfs(i, -1)
        return com_num
