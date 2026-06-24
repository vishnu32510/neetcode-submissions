class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1]
        right = [1]
        ans = [0] * n

        for i in range(1, n):
            left.append(left[-1] * nums[i-1])
            right.append(right[-1] * nums[n - i])
        for i in range(n):
            ans[i] = left[i] * right[n - i - 1]
        return ans