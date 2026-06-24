class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def binarySearch(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        l = 0
        r = n - 1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        res = binarySearch(0, pivot - 1)
        if res != -1:
            return res
        return binarySearch(pivot, n - 1)

        # Binary Search (O(logn), O(1)) - One pass

        # left = 0
        # right = n - 1

        # while left <= right:
        #     mid = (left + right) // 2

        #     if nums[mid] == target:
        #         return mid
            
        #     if nums[left] <= nums[mid]:
        #         if target < nums[left] or target > nums[mid]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     else:
        #         if target > nums[right] or target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        # return -1



        # Brute Force (O(n), O(1))

        # for i in range(n):
        #     if nums[i] == target:
        #         return i
        # return -1