class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        has = defaultdict(list)

        for s in strs:
            sor = ''.join(sorted(s))
            print(sor)
            has[sor].append(s)
        return has.values()
        
            