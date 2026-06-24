class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = defaultdict(int)

        for num in nums:
            dup[num] += 1
            if dup[num] == 2:
                return True
        return False