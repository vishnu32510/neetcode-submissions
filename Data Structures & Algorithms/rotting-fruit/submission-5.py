class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        fresh = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])
                    visit.add((i,j))
        
        minutes = 0
        if fresh == 0:
            return 0

        def addRotten(i, j):
            if i < 0 or j < 0 or j == n or i == m or (i,j) in visit or grid[i][j] != 1:
                return
            q.append([i,j])
            visit.add((i,j))
            nonlocal fresh
            fresh -= 1
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addRotten(r + 1,c)
                addRotten(r,c + 1)
                addRotten(r - 1,c)
                addRotten(r,c - 1)
            if q:
                minutes += 1

        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) not in visit and grid[i][j] == 1:
        #             return -1
        return minutes if fresh == 0 else -1




