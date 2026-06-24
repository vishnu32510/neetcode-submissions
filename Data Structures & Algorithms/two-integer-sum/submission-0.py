class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = defaultdict(int)
        n = len(nums)
        for i in range(n):
            if nums[i] in has:
                return [has[nums[i]], i]
            dif = target - nums[i]
            has[dif] = i
            
        return 