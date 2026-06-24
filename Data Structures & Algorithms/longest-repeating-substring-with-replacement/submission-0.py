class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        has = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            has[s[r]] += 1

            if (r - l + 1) - max(has.values()) > k:
                has[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
