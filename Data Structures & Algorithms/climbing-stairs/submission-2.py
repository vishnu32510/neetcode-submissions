class Solution:
    def climbStairs(self, n: int) -> int:
        # Time O(n) Space O(n)
        memo = {}
        def backtrack(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            
            if i in memo:
                return memo[i]
            
            return backtrack(i + 1) + backtrack(i + 2)
        
        
        return backtrack(0)