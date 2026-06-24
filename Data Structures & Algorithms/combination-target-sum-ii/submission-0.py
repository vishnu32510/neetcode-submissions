class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        sol = []
        n = len(candidates)

        def backtrack(i, total):
            if total == target:
                if sol not in res:
                    res.append(sol[:])
                return
            if total > target or i >= n:
                return
            
            sol.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            sol.pop()

            backtrack(i + 1, total)

        backtrack(0, 0)
        return res