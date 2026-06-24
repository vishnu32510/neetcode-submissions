class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[r] = nums[i]
                r += 1
        return r
            


            