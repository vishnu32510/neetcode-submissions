from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        # Time O(n^2) Space O(n)

        @lru_cache(None)
        def backtrack(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            
            return backtrack(i + 1) + backtrack(i + 2)
        
        
        return backtrack(0)