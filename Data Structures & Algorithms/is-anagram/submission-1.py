class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        s_has = defaultdict(int)
        t_has = defaultdict(int)
        n = len(s)
        m = len(t)
        if n != m:
            return False

        for i in range(n):
            s_has[s[i]] += 1
            t_has[t[i]] += 1
        for k, v in s_has.items():
            if v != t_has[k]:
                return False
        return True