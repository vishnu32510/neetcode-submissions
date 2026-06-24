class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        sol = []
        n = len(digits)
        def backtrack(i):
            if n == i:
                res.append("".join(sol))
                return
            
            for c in digitToChar[digits[i]]:
                sol.append(c)
                backtrack(i + 1)
                sol.pop()
        
        backtrack(0)
        return res