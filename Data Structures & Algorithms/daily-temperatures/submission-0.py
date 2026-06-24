class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = []
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[i] < temperatures[j]:
                    results.append(j - i)
                    break
                if j == n - 1:
                    results.append(0)
            if i == n - 1:
                    results.append(0)
        return results