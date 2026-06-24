class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        l = 0

        for c in t:
            if l == len(s) - 1:
                return True
            if c == s[l]:
                l += 1
        return False