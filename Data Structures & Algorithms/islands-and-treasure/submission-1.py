class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        INF = 2147483647
        visit = set()

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))

        def addRoom(r,c):
            if r < 0 or r == m or c < 0 or c == n or (r,c) in visit or grid[r][c] == -1:
                return
            visit.add((r,c))
            q.append([r,c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r, c + 1)
                addRoom(r - 1, c)
                addRoom(r, c - 1)
            
            dist += 1
            

        # BFS
        

        # DFS Brute Force Time (mn)^2 Space (mn)

        # def dfs(i, j, dist):
        #     if i < 0 or i > m - 1 or j < 0 or j > n - 1 or visited[i][j]:
        #         return INF
            
        #     if grid[i][j] == -1:
        #         return INF

        #     if grid[i][j] == 0:
        #         return dist

        #     visited[i][j] = True
        #     res = INF
        #     dist += 1
        #     res = min(dfs(i + 1, j, dist), dfs(i, j + 1, dist),dfs(i - 1, j, dist), dfs(i, j - 1, dist))
        #     visited[i][j] = False
        #     return res


        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == INF:
        #             grid[i][j] = dfs(i, j, 0)

