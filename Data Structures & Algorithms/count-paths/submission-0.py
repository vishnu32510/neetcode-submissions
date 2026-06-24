class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(x,y):
            if x >= m or y >= n or x < 0 or y < 0:
                return 0
            if x == m - 1 and y == n - 1:
                return 1
            
            return dfs(x, y + 1) + dfs(x + 1, y)
        
        return dfs(0, 0)
            