class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(n) O(1)
        n = len(cost)
        one, two = cost[n - 2], cost[n - 1]
        for i in range(n - 3, -1, -1):
            one, two = cost[i] + min(one, two), one
        return min(one,two)

        # O(n) O(n)
        # n = len(cost)
        # dp = [0] * (n + 1)
        # for i in range(2, n + 1):
        #     dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # return dp[n]

        
        # O(n) O(n)
        # n = len(cost)
        # memo = [-1] * (n)
        # def backtrack(i):
        #     if i >= n:
        #         return 0
            
        #     if memo[i] != -1:
        #         return memo[i]
            
        #     return cost[i] + min(backtrack(i + 1), backtrack(i + 2))
        # backtrack(0)
        # return min(backtrack(0), backtrack(1))