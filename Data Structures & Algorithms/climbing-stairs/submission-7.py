class Solution:
    def climbStairs(self, n: int) -> int:
        
        #O(n) O(1)
        one, two = 1, 1

        for i in range(2, n + 1):
            one, two = one + two, one
        return one

        #O(n) O(n)
        # dp = [0] * (n + 1)
        # dp[0], dp[1] = 1, 1
        # for i in range(2, n + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[n]

        # # Time O(n) Space O(n) - Memoization - Top Down
        # memo = defaultdict(lambda: -1)
        # def backtrackToTopDown(i):
        #     if i == n:
        #         return 1
        #     elif i > n:
        #         return 0
            
        #     if memo[i] != -1:
        #         return memo[i]
            
        #     memo[i] = backtrackToTopDown(i + 1) + backtrackToTopDown(i + 2)
        #     return memo[i]
        
        
        # return backtrackToTopDown(0)