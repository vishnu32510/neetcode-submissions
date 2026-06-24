class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = defaultdict(list)

        for s in strs:
            srted = "".join(sorted(s))
            anags[srted].append(s)

        return list(anags.values())