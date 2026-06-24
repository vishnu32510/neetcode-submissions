class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        area = [0]
        max_area = 0

        def dfs(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return

            if grid[i][j] == 0:
                return

            area[0] += 1
            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                area[0] = 0
                dfs(i, j)
                max_area = max(area[0], max_area)
        return max_area 

