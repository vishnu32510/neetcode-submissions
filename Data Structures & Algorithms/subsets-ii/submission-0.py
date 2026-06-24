class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sol = []
        n = len(nums)

        def backtrack(i):
            if i == n:
                if sol not in res:
                    res.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            backtrack(i + 1)
        
        backtrack(0)
        return res