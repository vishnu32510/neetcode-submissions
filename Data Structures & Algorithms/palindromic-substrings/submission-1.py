class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            l, r = i , i
            while l >= 0 and r < n:
                if self.isPalindrome(s[l:r + 1]):
                    cnt += 1
                l -= 1
                r += 1
            
            l, r = i , i + 1
            while l >= 0 and r < n:
                if self.isPalindrome(s[l:r + 1]):
                    cnt += 1
                l -= 1
                r += 1
        return cnt

        # Brute O(n^3) O(1)
        # for i in range(n):
        #     for j in range(i, n):
        #         if self.isPalindrome(s[i: j + 1]):
        #             cnt += 1
        # return cnt


            
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]