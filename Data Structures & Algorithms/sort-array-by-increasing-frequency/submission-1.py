class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freqList = [(value, -key) for key, value in freq.items()]

        freqList.sort()
        res = []
        for freq, num in freqList:
            for i in range(freq):
                res.append(-num)
        return res