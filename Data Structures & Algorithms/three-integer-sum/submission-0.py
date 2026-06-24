class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                summ = nums[j] + nums[k]
                if summ == target:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif summ > target:
                    k -= 1
                else:
                    j += 1
        return res