class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sSet = set()
        n = len(s)
        l = 0
        longest = 0
        for i in range(n):
            while s[i] in sSet:
                sSet.remove(s[l])
                l += 1
            sSet.add(s[i])
            longest = max(longest, i - l + 1)
        return longest