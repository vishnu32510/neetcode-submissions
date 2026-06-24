class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n):
            for j in range(i, n):
                if self.isPalindrome(s[i: j + 1]):
                    cnt += 1
        return cnt


            
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]