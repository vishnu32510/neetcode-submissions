class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        res = 0

        while r < n:
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                res = max(res, prof)
            else:
                l = r
            r += 1
        return res


        # # Brute Force
        # max_prof = 0
        # n = len(prices)
        # for i in range(n):
        #     buy = prices[i]
        #     for j in range(i + 1, n):
        #         sell = prices[j]
        #         max_prof = max(max_prof, sell - buy)
        # return max_prof