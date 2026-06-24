class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # O(n) O(n)
        n = len(cost)
        memo = [-1] * (n)
        def backtrack(i):
            if i >= n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            return cost[i] + min(backtrack(i + 1), backtrack(i + 2))
        backtrack(0)
        return min(backtrack(0), backtrack(1))