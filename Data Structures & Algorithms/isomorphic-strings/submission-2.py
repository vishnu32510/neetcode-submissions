class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st, map_ts = {}, {}

        if len(s) != len(t):
            return False

        for a, b in zip(s,t):
            if (a in map_st and map_st[a] != b) or (b in map_ts and map_ts[b] != a):
                return False
            map_st[a] = b
            map_ts[b] = a
        return True
                
