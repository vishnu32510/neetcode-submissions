class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        max_odd = 0
        min_even = float('inf')
        for key, value in freq.items():
            if value % 2 == 0:
                min_even = min(min_even, value)
            else:
                max_odd = max(max_odd, value)
        return (max_odd - min_even)
        