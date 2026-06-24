class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)

        while i < n and j < n:
            nums[i] = nums[j]
            while j < n and nums[j] == nums[i]:
                j += 1
            i += 1
        return i