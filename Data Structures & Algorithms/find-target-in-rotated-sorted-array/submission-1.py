class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # Binary Search

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1



        # Brute Force (O(n), O(1))

        # for i in range(n):
        #     if nums[i] == target:
        #         return i
        # return -1