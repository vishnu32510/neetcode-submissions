class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        max_seq = 0
        cons = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            if nums[i - 1] + 1 == nums[i]:
                cons += 1
                print(cons)
            else:
                max_seq = max(max_seq, cons)
                cons = 1
        return max(max_seq, cons)
            