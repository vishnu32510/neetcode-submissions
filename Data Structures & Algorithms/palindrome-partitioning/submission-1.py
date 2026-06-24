class Solution:
    def isPalindrome(self,s, l ,r) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        sol = []

        def backtrack(i):
            if i >= n:
                res.append(sol[:])
                return
            
            for j in range(i,n):
                if self.isPalindrome(s, i, j):
                    sol.append(s[i : j + 1])
                    backtrack(j + 1)
                    sol.pop()

        backtrack(0)
        return res