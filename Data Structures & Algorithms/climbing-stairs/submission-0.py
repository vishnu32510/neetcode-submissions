class Solution:
    def climbStairs(self, n: int) -> int:
        sol = [0]

        def backtrack(i):
            if i == n:
                sol[0] += 1
                return
            elif i > n:
                return
            
            backtrack(i + 1)
            backtrack(i + 2)
            return
        
        backtrack(0)
        return sol[0]