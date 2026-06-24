class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        res, resLen = "", 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s[i:j + 1]) and resLen < (j - i + 1):
                    res = s[i:j+1]
                    resLen = j - i + 1
            
        return res

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]