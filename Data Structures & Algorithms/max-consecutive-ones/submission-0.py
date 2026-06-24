class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        i = 0
        while i < len(nums):
            ones = 0
            while i < len(nums) and nums[i] == 1:
                ones += 1
                i += 1

            max_ones = max(max_ones, ones) 
            i += 1
        return max_ones