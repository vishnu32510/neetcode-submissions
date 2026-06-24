class Solution:
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        resIdx, resLen = 0, 0
        n = len(s)

        # dp = [[False] * n for _ in range(n)]

        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):
        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True
        #             if resLen < (j - i + 1):
        #                 resIdx = i
        #                 resLen = j - i + 1
        # print(dp)

        # return s[resIdx : resIdx + resLen]

        # Two Pointer Expanding (O(n^2) O(1))
        for i in range(n):

            r, l = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if resLen < (r - l + 1):
                    resLen = r - l + 1
                    resIndex = l
                l -= 1
                r += 1

            r, l = i + 1, i
            while l >= 0 and r < n and s[l] == s[r]:
                if resLen < (r - l + 1):
                    resLen = r - l + 1
                    resIndex = l
                l -= 1
                r += 1
        return s[resIndex: resIndex + resLen]


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