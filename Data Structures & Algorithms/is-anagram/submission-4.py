
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a_hash = defaultdict(int)

        for c1, c2 in zip(s,t):
            a_hash[c1] += 1
            a_hash[c2] -= 1
        print(a_hash)
        for k, v in a_hash.items():
            if v != 0:
                return False
        return True




        