class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

        # memo = [[-1] * n for _ in range(m)]
        # def dfs(x,y):
        #     if x == m - 1 and y == n - 1:
        #         return 1
        #     if x >= m or y >= n or x < 0 or y < 0:
        #         return 0
        #     if memo[x][y] != -1:
        #         return memo[x][y]
            
        #     memo[x][y] = dfs(x, y + 1) + dfs(x + 1, y)
        #     return memo[x][y]
        
        # return dfs(0, 0)
            