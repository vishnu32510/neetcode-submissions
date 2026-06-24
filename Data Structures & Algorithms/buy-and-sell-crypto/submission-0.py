class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        max_prof = 0
        n = len(prices)
        for i in range(n):
            buy = prices[i]
            for j in range(i + 1, n):
                sell = prices[j]
                max_prof = max(max_prof, sell - buy)
        return max_prof