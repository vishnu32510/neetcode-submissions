class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        def dfs(x,y):
            if x == m - 1 and y == n - 1:
                return 1
            if x >= m or y >= n or x < 0 or y < 0:
                return 0
            if memo[x][y] != -1:
                return memo[x][y]
            
            memo[x][y] = dfs(x, y + 1) + dfs(x + 1, y)
            return memo[x][y]
        
        return dfs(0, 0)
            