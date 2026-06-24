class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        # Two Pointer Expanding O(n^2) O(1)
        for i in range(n):
            l, r = i , i
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            
            l, r = i , i + 1
            while l >= 0 and r < n and s[l] == s[r]:
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