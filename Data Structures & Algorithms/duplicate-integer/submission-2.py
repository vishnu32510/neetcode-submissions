class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_set = set()

        for num in nums:
            if num in has_set:
                return True
            has_set.add(num)
        return False