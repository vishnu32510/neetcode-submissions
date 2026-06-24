class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp,i))
        return res
        # Brute Force
        # n = len(temperatures)
        # results = []
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[i] < temperatures[j]:
        #             results.append(j - i)
        #             break
        #         if j == n - 1:
        #             results.append(0)
        #     if i == n - 1:
        #             results.append(0)
        # return results