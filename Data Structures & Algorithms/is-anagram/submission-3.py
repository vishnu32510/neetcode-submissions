from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ang = defaultdict(int)
        for c1, c2 in zip(s,t):
            ang[c1] += 1
            ang[c2] -= 1
        
        for key, value in ang.items():
            if value != 0:
                return False
        return True

