class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        # maxHeap = [-num for num in nums]
        # heapq.heapify(maxHeap)
        # i = 0
        # ans = 0
        # while i < k:
        #     ans = heapq.heappop(maxHeap)
        #     i += 1
        # return -ans