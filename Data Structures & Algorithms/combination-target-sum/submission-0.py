class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)

        def backtrack(i):
            if sum(sol) == target:
                res.append(sol[:])
                return 
            if sum(sol) > target:
                return
            if i == n:
                return
            
            sol.append(nums[i])
            backtrack(i)
            sol.pop()

            backtrack(i + 1)
        
        backtrack(0)
        return res