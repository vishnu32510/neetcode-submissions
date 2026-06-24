class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        n = len(s)
        res, resLen = "", 0
        for i in range(n):

            r, l = i, i
            while l >= 0 and r < n:
                if self.isPalindrome(s[l:r + 1]) and resLen < (r - l + 1):
                    resLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1

            r, l = i + 1, i
            while l >= 0 and r < n:
                if self.isPalindrome(s[l:r + 1]) and resLen < (r - l + 1):
                    resLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res


        # Brute Force (O(n^3), O(n)) 
        # res, resLen = "", 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if self.isPalindrome(s[i:j + 1]) and resLen < (j - i + 1):
        #             res = s[i:j+1]
        #             resLen = j - i + 1
            
        # return res

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True