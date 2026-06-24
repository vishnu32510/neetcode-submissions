class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        memo = {}
        def dfs(value):
            if value == 0:
                return 0
            if value in memo:
                return memo[value]
            res = 10001
            for coin in coins:
                if (value - coin) >= 0:
                    res = min(res, 1 + dfs(value - coin))
            memo[value] = res
            return res
        minCoins = dfs(amount)
        return minCoins if minCoins != 10001 else -1