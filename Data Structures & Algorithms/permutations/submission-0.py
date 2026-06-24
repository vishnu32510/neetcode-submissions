class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)

        def backtrack(i, pick):
            if i == n:
                res.append(sol[:])
                return
            
            for j in range(n):
                if not pick[j]:
                    pick[j] = True
                    sol.append(nums[j])
                    backtrack(i + 1, pick)
                    sol.pop()
                    pick[j] = False

        
        backtrack(0, [False] * n)
        return res