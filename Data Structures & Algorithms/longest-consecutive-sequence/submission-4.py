class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
            

        # T: O(N)
        # S: O(1)
        # if len(nums) == 0:
        #     return 0
        # nums.sort()
        # max_seq = 0
        # cons = 1
        # for i in range(1, len(nums)):
        #     if nums[i - 1] == nums[i]:
        #         continue
        #     if nums[i - 1] + 1 == nums[i]:
        #         cons += 1
        #     else:
        #         max_seq = max(max_seq, cons)
        #         cons = 1
        # return max(max_seq, cons)
            