class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = [(value, -key) for key, value in freq.items()]

        heap.sort()
        res = []
        while heap:
            freq, num = heapq.heappop(heap)
            for i in range(freq):
                res.append(-num)
        return res