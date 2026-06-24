class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s,t):
            map_c = {}

            if len(s) != len(t):
                return False

            for a, b in zip(s,t):
                if a in map_c and map_c[a] != b:
                    return False
                map_c[a] = b
            return True
        
        return helper(s,t) and helper(t,s)
                
