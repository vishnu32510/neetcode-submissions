class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)

        for i in range(0,len(s2) - k + 1):
            if sorted(s1) == sorted(s2[i: i + k]):
                return True
        return False