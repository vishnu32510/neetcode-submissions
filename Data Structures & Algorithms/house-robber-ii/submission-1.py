class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def h_rob(arr):
            rob1 = 0
            rob2 = 0
            n = len(arr)
            for i in range(n):
                temp = max(rob1 + arr[i], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(h_rob(nums[:- 1]), h_rob(nums[1:]))