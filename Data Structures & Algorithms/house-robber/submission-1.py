class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2 = 0, 0

        # for num in nums:
        #     temp = max(num + rob1, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        
        # return rob2
        n = len(nums)
        memo = {i:-1 for i in range(n)}
        def dfs(i):
            if i >= n:
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        return dfs(0)