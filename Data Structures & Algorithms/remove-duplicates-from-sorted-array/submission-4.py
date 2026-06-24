class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
        # i = 0
        # j = 0
        # n = len(nums)

        # while i < n and j < n:
        #     nums[i] = nums[j]
        #     while j < n and nums[j] == nums[i]:
        #         j += 1
        #     i += 1
        # return i